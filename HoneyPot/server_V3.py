#ssh localhost -p 2292
#ssh -p 2292 kyle@192.168.98.99 

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

    def check_auth_password(self, username, password):
        #Change the number of allowed attempts for a real scenario
        while True:
            file.write(str(password) + "\n")
            print(password)
            if password == "HelloWorld":
                return paramiko.AUTH_SUCCESSFUL
            else:
                return paramiko.AUTH_FAILED
                
    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        else:
            return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_shell_request(self, channel):
        return True 

    def check_channel_exec_request(self, channel, command):
        command_list = {
            "ls": "file1.txt file2.log \n",
            "whoami": "root\n",
            "pwd": "/home/user\n",
        }
        response = command_list.get(command.strip())

        if response != None:
            channel.send(response)
            return True

        else:   
            channel.send("Start inputting commands:\n")
            return True
    
def inputCommands():
    channel.send("Welcome to SSH Server\n")
    while True:
        #print("called 1")
        command = channel.recv(1024).decode().strip()
        file.write(str(command) + "\n")
        print(command)
        if command != "exit":
            SSHServer.check_channel_exec_request(SSHServer, channel=channel, command=command)
        else: 
            channel.close()
            file.close()
            break

def log():
    count = 0
    file = open("log" + str(count) + ".txt", "w")
                
if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server.bind(('0.0.0.0', 2292))
    server.listen()
    print("Listening...")

    while True:
        file = open("log.txt", "w")

        logging = threading.Thread(target=log, args=())
        logging.start()
        
        clientSocket, clientAddr = server.accept()

        file.write("New Connection From {addr}\n".format(addr = clientAddr))
        print("New Connection From {addr}".format(addr = clientAddr))
        transport = paramiko.Transport(clientSocket)
    
        key = paramiko.RSAKey.from_private_key_file('Honeypot')
        transport.add_server_key(key) 
        myServer = SSHServer()

        transport.start_server(server=myServer)
        channel = transport.accept(20)

        #Fix issue with relogging in here
        inputCommands = threading.Thread(target=inputCommands, args=())
        inputCommands.start()
