import paramiko
import socket
import os

class SimpleServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        if username == 'testuser' and password == 'password123':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_channel_request(self, kind, channel):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

# Set up the SSH server
def start_server():
    host = 'localhost'
    port = 22
    private_key_path = '/path/to/private/key'  # Path to your private key file
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Listening for SSH connections on {host}:{port}...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    
    transport = paramiko.Transport(client_socket)
    transport.load_server_moduli()
    
    # Provide private key for authentication
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    transport.add_server_key(private_key)
    
    # Start the SSH server
    server = SimpleServer()
    transport.start_server(server=server)

    # Wait for client to authenticate
    channel = transport.accept(20)
    
    if channel is None:
        print("Authentication failed.")
        transport.close()
        return
    
    print("Client authenticated successfully.")
    
    # Here, initiate the SFTP session once authentication is successful
    try:
        sftp_server = paramiko.SFTPServerInterface(channel)
        sftp_server.start_server()
        print("SFTP server started.")
    except Exception as e:
        print(f"Failed to start SFTP server: {e}")
    
    return transport


if __name__ == '__main__':
    start_server()
