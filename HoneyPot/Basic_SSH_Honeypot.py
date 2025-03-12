#ssh localhost -p 2292
#ssh -p 22 kyle@0.0.0.0

import socket 
import threading 
import paramiko
#Remember to uninstall the cryptography 
#Remember to uninstall bcrypt 
#Remember to uninstall nacl 
#Remember to uninstall pynacl

count = 0
class SSHServer(paramiko.ServerInterface):

    def check_auth_password(self, username, password):
        #Change the number of allowed attempts for a real scenario
        while True:
            global file
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
        return True
    
    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return False

def inputCommands(): 
    global file
    command_list = {
        "ls": "file1.txt file2.log \n",
        "whoami": "root\n",
        "pwd": "/home/user\n",
    }
        
    channel.send("Start Inputting Your Commands:\r\n")
    while True:
        command = channel.recv(1024)
        if command != None:
            command = command.decode('utf-8')
            if command != "exit\n":
                response = command_list.get(command.strip())
                if response != None:
                    print(command.strip())
                    file.write(command)
                    channel.send(response)
                    
                else:
                    channel.send("Invalid Command\n")
                    print(command.strip())
                    file.write(command)

            else:
                print(command.strip())
                file.write(command)
                file.close()
                break
            


if __name__ == "__main__":

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server.bind(('0.0.0.0', 22))
    server.listen()
    print("Listening...")

    while True:
        clientSocket, clientAddr = server.accept()
        
        #Creates a new file to log the users activities
        #print(count)
        count = count + 1
        file = open("log" + str(count) + ".txt", "w")

        file.write("New Connection From {addr}\n".format(addr = clientAddr))
        print("New Connection From {addr}".format(addr = clientAddr))

        transport = paramiko.Transport(clientSocket)
        key = paramiko.RSAKey.from_private_key_file('/Users/kyle/Documents/GitHub/kyle-ritchie/HoneyPot/Honeypot')
        transport.add_server_key(key) 
        myServer = SSHServer()
        transport.start_server(server=myServer)
        
        channel = transport.accept(20)
        channel.send("Welcome to SSH Server\r\n")

        inputCommands()
        channel.close()
