import socket 
import struct 

def IP_Packet(raw_data):
    version, IHL, TOS, len = struct.unpack()

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW)

    print("Programming Running")
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, dataETH = IP_Packet(raw_data)

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