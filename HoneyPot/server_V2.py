#ssh localhost -p 2292

import socket 
import threading 
import paramiko
import os
from datetime import datetime
#Remember to uninstall the cryptography 
#Remember to uninstall bcrypt 
#Remember to uninstall nacl 
#Remember to uninstall pynacl

def fileHandling(sftpServer):
    #Create SFTP client
    #sftpClient = paramiko.SFTPClient.from_transport(newClient)
    fileName = "Balls.txt"

    #Upload a file to the server
    sftpClient.put('temp.jpg', fileName)

    #List from the servers local directory
    print(sftpClient.listdir())

    #Get the file
    sftpClient.get(fileName, fileName)

    #Remove the file
    sftpClient.remove(fileName)

    #List files 
    print('*' * 80)
    print(sftpClient.listdir())

    input()

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

        newClient = paramiko.Transport(clientSocket)

        #key = paramiko.RSAKey.generate(2048)
        key = paramiko.RSAKey.from_private_key_file('Honeypot')
        newClient.add_server_key(key) 
        myServer = SSHServer(clientSocket, clientAddr)
        #myServer.check_port_forward_request()
        newClient.start_server(server=myServer)
        channel = newClient.accept(20)

        sftpServer = paramiko.SFTPServerInterface(channel)
        print("SFTP server has started")

        fileHandling(sftpServer)


        

        #session = paramiko.SSHClient()
        #session._transport = transport

        # Run a command on the server (like listing files)
        #stdin, stdout, stderr = session.exec_command('ls /path/to/directory')
        #files = stdout.read().decode()
        #print(files)

        # Close session
        #session.close()
        #transport.close()




