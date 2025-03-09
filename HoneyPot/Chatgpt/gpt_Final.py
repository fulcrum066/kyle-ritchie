import paramiko
import socket
import threading
import logging
import os

# Setup logging
logging.basicConfig(filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

class SSHHoneypot(paramiko.ServerInterface):
    def __init__(self):
        super().__init__()
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        logging.info(f"Login attempt - Username: {username}, Password: {password}")
        return paramiko.AUTH_SUCCESSFUL  # Always allow login

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_shell_request(self, channel):
        logging.info("Shell access requested.")
        channel.send(b"Fake shell active. Type commands:\n$ ")
        return True

    def check_channel_exec_request(self, channel, command):
        logging.info(f"Command attempted: {command}")

        # Fake command responses
        fake_responses = {
            "ls": "file1.txt\nfile2.log\nconfig.yaml\n",
            "whoami": "root\n",
            "pwd": "/home/user\n",
            "uname -a": "Linux honeypot 5.4.0-91-generic #102-Ubuntu SMP Fri Nov 5 11:37:01 UTC 2021 x86_64 GNU/Linux\n"
        }

        response = fake_responses.get(command.strip(), "bash: command not found\n")
        channel.send(response.encode())
        channel.close()
        return True

# Start SSH Server
def start_ssh_server():
    host_key = paramiko.RSAKey.generate(2048)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 2222))  # Run on port 2222
    server_socket.listen(100)

    while True:
        client_socket, addr = server_socket.accept()
        logging.info(f"New connection from {addr}")

        transport = paramiko.Transport(client_socket)
        transport.add_server_key(host_key)
        server = SSHHoneypot()

        try:
            transport.start_server(server=server)
            channel = transport.accept(20)
            if channel is None:
                continue

            channel.send(b"Welcome to Fake SSH Server!\n")
            while True:
                command = channel.recv(1024).decode().strip()
                if not command or command.lower() == "exit":
                    break
                logging.info(f"Executed command: {command}")
                response = f"Fake output for: {command}\n"
                channel.send(response.encode())
            channel.close()
        except Exception as e:
            logging.error(f"Error: {str(e)}")
        finally:
            transport.close()

if __name__ == "__main__":
    print("SSH Honeypot running on port 2222...")
    start_ssh_server()
