# Jared Wightman


import socket as s
import threading



HOST = s.gethostbyname(s.gethostname())
FOREIGN = open("C:/Users/JWigh/source/repos/Local Networking IP.txt", "r").readline()
PORT = 60001
hostName = s.gethostname()


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
    fileName = serverNode.recv(4096).decode()
    fileData = serverNode.recv(4096).decode()
    print("File: ", fileName)
    file = open((directory + fileName), "w")
    file.write(fileData)
    file.close()
    serverNode.sendall("File received.".encode())
    


def sendFile(clientNode):
    
    fileName = input("Enter file name below.       (SHORTCUTS: APPLE, TEXTDOC, WORDDOC)\n")
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
        file = open(fileSource, "r")
        fileData = file.read()
        print("Sending file...       (SOURCE: ", fileSource, ")")
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
    remoteName = remote.recv(4096).decode()
    print("CONNECTED TO REMOTE: ", remoteName, "\n")
    
    # Receives data from foreign client
    try:
        while True:

            received = remote.recv(4096).decode()
            if received == "FILE":
                recvFile(serverNode)

            else:
                print(remoteName, ": ", received)
    
    except:
        print("\nCONNECTION TERMINATED BY REMOTE.")
        
# Thread to set up as a client and connect to a server. This is the "sending" side of the script.
def client():
    
    # Setting up client node, connecting to the foreign computer's server node, telling other computer this one's name
    clientNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    clientNode.connect((FOREIGN, PORT))
    clientNode.sendall(hostName.encode())

    # Sends data to foreign server
    while True:
        
        toSend = input()
        match toSend:
            case "SENDFILE":
                sendFile(clientNode)
            case "EXIT":
                raise SystemExit # FIX THIS, MAKES OTHER END GO STUPID MODE
            case _:
                clientNode.sendall(toSend.encode())


        

# Defining seperate threads (functions above) and starting them
serverThread = threading.Thread(target=server)        
clientThread = threading.Thread(target=client)
serverThread.start()
clientThread.start()



