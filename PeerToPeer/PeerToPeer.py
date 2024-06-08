# Jared Wightman


import socket as s
import threading


HOST = s.gethostbyname(s.gethostname())
FOREIGN = open("C:/Users/JWigh/source/repos/Local Networking IP.txt", "r").readline()
PORT = 60001



def TEMPFILEREADWRITE(): # For reference, delete later
    file1 = open("C:/Users/JWigh/source/repos/txtTest.txt", "r")
    file1data = file1.read()
    newFileName = "NewFile.txt"
    file2 = open(newFileName, "w")
    file2.write(file1data)
    file2.close()


def recvFile(serverNode):
    
    directory = "C:/Users/JWigh/source/repos/"
    print("Receiving file...")
    fileName = serverNode.recv(4096)
    fileData = serverNode.recv(4096)
    print("File: ", fileName)
    file = open((directory + fileName), "w")
    file.write(fileData)
    file.close()
    serverNode.sendall("File received.".encode())
    


def sendFile(clientNode):
    
    fileName = input("What image would you like to send?")
    fileType = ""

    match fileName:
        case "APPLE":
            fileSource = "C:/Users/JWigh/source/repos/apple.jpg"
            fileName = ".jpg"
            
        case "TEXTDOC":
            fileSource = "C:/Users/JWigh/source/repos/txtTest.txt"
            fileName = "txt"
            
        case "WORDDOC":
            fileSource = "C:/Users/JWigh/source/repos/wordTest.docx"
            fileName = ".docx"
        
        case _:
            fileSource = fileName
            fileName = ".txt" # default
    
    try:
        print(fileSource) #
        file = open(fileSource, "r")
        fileData = file.read()
        print("Sending file...")
        clientNode.sendall("FILE".encode())
        clientNode.sendall(fileName.encode())
        clientNode.sendall(fileData.encode())
        file.close()
        print("File sent!")



    except FileNotFoundError:
        print("File could not be opened.")
    except s.error:
        print("File could not be sent.")
    except:
        print("An error occurred.")
        



# Thread to set up as a server and allow a client to connect. This is the "receiving" side of the script.
def server():
    
    # Setting up server node, connecting to the foreign computer's client node
    serverNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    serverNode.bind((HOST, PORT))
    serverNode.listen()
    remote, remote_address = serverNode.accept()
    remoteName = remote.gethostname()
    print("CONNECTED TO REMOTE: ", remoteName, "\n")
    
    # Receives data from foreign client
    while True:

        received = remote.recv(4096)
        if received == "FILE":
            recvFile(serverNode)

        else:
            print(remoteName, ": ", received.decode())
        
# Thread to set up as a client and connect to a server. This is the "sending" side of the script.
def client():
    
    # Setting up client node, connecting to the foreign computer's server node
    clientNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    clientNode.connect((FOREIGN, PORT))
    
    # Sends data to foreign server
    while True:
        
        toSend = input()
        match toSend:
            case "SENDFILE":
                sendFile(clientNode)
            case "EXIT":
                print("Exiting...")
                clientNode.close() # Which one? All three?
                clientNode.shutdown() # 
                exit # 
            case _:
                clientNode.sendall(toSend.encode())


        

# Defining seperate threads (functions above) and starting them
serverThread = threading.Thread(target=server)        
clientThread = threading.Thread(target=client)
serverThread.start()
clientThread.start()



