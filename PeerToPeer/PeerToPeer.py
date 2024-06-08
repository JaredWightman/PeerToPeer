# Jared Wightman

# DESKTOP IPv4: 10.105.178.207
# LAPTOP IPv4:  10.105.201.165
# PORT:         60001


import socket as s

HOST = s.gethostbyname(s.gethostname())
PORT = 60001

FOREIGN = ""

if HOST == "10.105.178.207":
    FOREIGN = "10.105.201.165"
elif HOST == "10.105.201.165":
    FOREIGN = "10.105.178.207"


node = s.socket(s.AF_INET, s.SOCK_STREAM)
node.bind((HOST, PORT))

node.listen()
node.connect((FOREIGN, PORT))
remote, remoteAddress = node.accept()

while True: # Need to thread or sumn
    toSend = input("> ")
    node.sendall(toSend)
    received = remote.recv(1024)
    print("< ", received.decode())

# while 1:

#     command = input("> ")
#     match command.upper():
#         case "EXIT":
#             break
#         case "CONNECT":
#             foreignhost = input("CONNECT TO IP: ")
#             print("Attempting to connect to '{}'".format(foreignhost)) 
#             # Add loading dots here...threading?
#             node.connect((foreignhost, PORT))
#             # Raise error
            
#             node.sendall(b'Hello, server')
#             # Receive data from the server
#             data = node.recv(1024)

#             print('Received:', data.decode())
#         case "LISTEN":
#             print("Listening...")
#             node.listen()
#             # Accept a connection
#             remoteNode, addr = node.accept() # conn is the other socket!

#             print('Connected by', addr)
#             while True:
#                 # Receive data from the client
#                 data = remoteNode.recv(1024)
#                 if not data:
#                     break
#                 print('Received:', data.decode())
#                 # Send a response back to the client
#                 remoteNode.sendall(data)


#     print("Cycled 'While' loop")