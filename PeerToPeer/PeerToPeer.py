# Jared Wightman

# DESKTOP IPv4: 10.105.178.207
# LAPTOP IPv4:  10.105.201.165
# PORT:         60001


import socket as s

HOST = s.gethostbyname(s.gethostname())
PORT = 60001


node = s.socket(s.AF_INET, s.SOCK_STREAM)
node.bind((HOST, PORT))


################
import socket

# Define the IP address and port to listen on
# HOST = '10.105.178.207'  # Localhost
# PORT = 60001       # Arbitrary port number

# Create a socket object
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     # Bind the socket to the address and port
#     s.bind((HOST, PORT))
#     # Listen for incoming connections
#     s.listen()

#     print("Waiting for connection...")

#     # Accept a connection
#     conn, addr = s.accept() # conn is the other socket!

#     with conn:
#         print('Connected by', addr)
#         while True:
#             # Receive data from the client
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print('Received:', data.decode())
#             # Send a response back to the client
#             conn.sendall(data)


#################


while 1:
    # add listen on seperate thread? so input doesn't block it?
    # node.listen()
    # (connection, address) = node.accept()


    command = input("> ")
    match command.upper():
        case "EXIT":
            break
        case "CONNECT":
            foreignhost = input("CONNECT TO IP: ")
            print("Attempting connection to '{}'".format(foreignhost)) 
            # Add loading dots here...threading?
            node.connect((foreignhost, PORT))
            # Raise error
            
            node.sendall(b'Hello, server')
            # Receive data from the server
            data = node.recv(1024)

            print('Received:', data.decode())
        case "LISTEN":
            print("Listening...")
            node.listen()
            # Accept a connection
            remoteNode, addr = node.accept() # conn is the other socket!

            with remoteNode:
                print('Connected by', addr)
                while True:
                    # Receive data from the client
                    data = remoteNode.recv(1024)
                    if not data:
                        break
                    print('Received:', data.decode())
                    # Send a response back to the client
                    remoteNode.sendall(data)


    print("Cycled 'While' loop")