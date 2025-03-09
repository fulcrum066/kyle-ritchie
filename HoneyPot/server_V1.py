#ssh localhost -p 2292

import socket 
import threading 
import paramiko
import pysftp as sftp
import crypto
import os
#Remember to uninstall the cryptography 
#Remember to uninstall bcrypt 
#Remember to uninstall nacl 
#Remember to uninstall pynacl

class SSHServer(paramiko.ServerInterface):
    def __init__(self, clientSocket, clientAddr):
        self.passAttempts = 0
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
        self.base_path = os.path.abspath("balls")

    def check_auth_password(self, username, password):
        #Change the number of allowed attempts for a real scenario
        while self.passAttempts < 2:
            print("Client: {ADDR}".format(ADDR = self.clientAddr, Password = password))
            if username == "kyle" and password == "Balls":
                self.passAttempts = 1000
                print("called 1")
                return paramiko.AUTH_SUCCESSFUL

            else:
                self.passAttempts = self.passAttempts + 1
                if self.passAttempts == 2:
                    return paramiko.AUTH_SUCCESSFUL
                else:
                    return paramiko.AUTH_FAILED
        
        return paramiko.AUTH_SUCCESSFUL
    
    def check_port_forward_request(self):
        print("2 called")
        return super().check_port_forward_request(self.clientAddr, self.clientAddr[1])


if __name__ =="__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server.bind(('0.0.0.0', 2292))
    server.listen()
    print("Listening...")

    while True:
        clientSocket, clientAddr = server.accept()

        print("New Connection From {addr}".format(addr = clientAddr))

        transport = paramiko.Transport(clientSocket)
        
        #key = paramiko.RSAKey.generate(2048)
        key = paramiko.RSAKey.from_private_key_file('Honeypot')
        transport.add_server_key(key) 
        myServer = SSHServer(clientSocket, clientAddr)
        myServer.check_port_forward_request()
        transport.start_server(server=myServer)




