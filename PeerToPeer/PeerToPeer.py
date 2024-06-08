# Jared Wightman

from pickle import TRUE
import socket as s
import threading


HOST = s.gethostbyname(s.gethostname())
FOREIGN = open("C:/Users/JWigh/source/repos/Local Networking IP.txt", "r").readline()
PORT = 60001

def server():
    
    serverNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    serverNode.bind((HOST, PORT))
    serverNode.listen()
    remote, remote_address = serverNode.accept()
    
    while True:

        received = remote.recv(1024)
        print(received.decode(), "> ")
            
def client():
    
    clientNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    clientNode.connect((FOREIGN, PORT))
    
    while True:
        
        to_send = input()
        clientNode.sendall(to_send.encode())


serverThread = threading.Thread(target=server)        
clientThread = threading.Thread(target=client)

serverThread.start()
clientThread.start()



