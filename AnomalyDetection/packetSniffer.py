import socket 
import struct 
from scapy.all import *
#Remember to uninstall scapy 
#sudo python3 packetSniffer.py

#unpack ethernet frame
def ethernet_frame(data):
    print("before " + str(data))
    dest_mac, src_mac, proto = struct.unpack('6s 6s H', data[:14])
    print("after " + str(data[:14]))
    print(dest_mac)
    print(src_mac)
    print(proto)
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

#Return properly formatted MAC address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    #Places everything to 2 decimal places
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr 

#Unpacks IPv4 packet
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4 
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, socket.htons(proto), ipv4(src), ipv4(target), data[header_length:]

#Returns properly formatted IPv4 address
def ipv4(addr): 
    return '.'.join(map(str, addr))

#Unpacks ICMP packet
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

#Unpacks TCP segment
def tcp_packet(data):
    (src_port, dest_port, sequence, acknowledgement, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 5
    flag_psh = (offset_reserved_flags & 8) >> 5
    flag_rst = (offset_reserved_flags & 4) >> 5
    flag_syn = (offset_reserved_flags & 2) >> 5
    flag_fin = (offset_reserved_flags & 1) >> 5
    return src_port, dest_port, sequence, acknowledgement, offset_reserved_flags, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset: ]

def packet_callback(packet):
    print(packet.show())

def main():
    sniff(iface="en0", prn=packet_callback, filter="ether", store=0)
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW)

    print("Programming Running")
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, dataETH = ethernet_frame(raw_data)

        print('Ethernet Frame: ')
        print("Destination: {}, Source {}, Protocol: {}".format(dest_mac, src_mac, eth_proto))
        eth_proto = int(eth_proto)

        if eth_proto == 2048:
            version, header_length, ttl, proto_IPv4, src, target, dataIPV = ipv4_packet(dataETH)
            print("Run 1")

            #Will the 'proto' variable contain a integer or string?
            #TCP
            if proto_IPv4 == 6: 
                src_port, dest_port, sequence, acknowledgement, offset_reserved_flags, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, dataTCP = tcp_packet(dataIPV)
                print("run 2")

            #ICMP
            elif proto_IPv4 == 1:
                icmp_type, code, checksum, data = icmp_packet(dataIPV)
                print("run 3") 
        
            else:
                print("Packet contained protocol other than ICMP or TCP")

        else:
            print("Packet contained protocol other than IPv4")



if __name__ == "__main__":
    main()