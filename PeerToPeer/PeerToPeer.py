# Jared Wightman

from pickle import TRUE
import socket as s
import threading


HOST = s.gethostbyname(s.gethostname())
FOREIGN = open("C:/Users/JWigh/source/repos/Local Networking IP.txt", "r").readline()
PORT = 60001
receiveCheck = True

def server():
    
    serverNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    serverNode.bind((HOST, PORT))
    serverNode.listen()
    remote, remote_address = serverNode.accept()
    global receiveCheck
    
    while True:

        received = remote.recv(1024)
        print(received.decode())
        receiveCheck = False
        print("Resetting receiveCheck")
        
            
def client():
    
    clientNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    clientNode.connect((FOREIGN, PORT))
    global receiveCheck
    
    while True:
        while receiveCheck:
            to_send = input("> ")
            clientNode.sendall(to_send.encode())
        receiveCheck = True
        print("Resetting input")


serverThread = threading.Thread(target=server)        
clientThread = threading.Thread(target=client)

serverThread.start()
clientThread.start()



