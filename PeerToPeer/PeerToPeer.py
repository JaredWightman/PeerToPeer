# Jared Wightman


from asyncio.windows_events import NULL
import socket as s
import threading



HOST = s.gethostbyname(s.gethostname())
FOREIGN = open("C:/Users/JWigh/source/repos/Local Networking IP.txt", "r").readline()
PORT = 60001
hostName = s.gethostname()


def recvFile(remote, serverNode):
    
    directory = "C:/Users/JWigh/source/repos/"
    print("Receiving file...")
    fileName = remote.recv(4096).decode()
    remote.sendall("r".encode())
    fileData = ""
    while True:
        fileData = remote.recv(4096).decode() ## remove decode?
        if fileData != "":
            break
        print("CHECK")
    print("File: ", fileName)
    file = open((directory + fileName), "w")
    file.write(fileData)
    file.close()
    remote.sendall("File received.".encode())
    


def sendFile(clientNode):
    
    fileName = input("Enter file name below.       (SHORTCUTS: TEXTDOC, WORDDOC, APPLE)\n")
    fileType = ""

    match fileName:
        case "APPLE":
            fileSource = "C:/Users/JWigh/source/repos/apple.jpg"
            fileName = "apple.jpg"
            
        case "TEXTDOC":
            fileSource = "C:/Users/JWigh/source/repos/txtTest.txt"
            fileName = "txtTest.txt"
            
        case "WORDDOC":
            fileSource = "C:/Users/JWigh/source/repos/wordTest.docx"
            fileName = "wordTest.docx"
        
        case _:
            fileSource = fileName
            fileName = "file.txt" # default
    
    try:
        file = open(fileSource, "r") ############### "r" to "rb"
        fileData = file.read()
        print("Sending file...       (SOURCE: ", fileSource, ")")
        clientNode.sendall("FILE".encode())
        
        clientNode.sendall((fileName).encode())
        while True:
            reception = clientNode.recv(4096).decode()
            if reception == "r":
                break
            print("check")
        clientNode.sendall(str(fileData).encode())#####
        file.close()
        print("File sent!")




    except FileNotFoundError:
        print("File could not be opened.")
    except s.error:
        print("File could not be sent.")
    # except:
    #     print("An error occurred.")
        



# Thread to set up as a server and allow a client to connect. This is the "receiving" side of the script.
def server():
    
    # Setting up server node, connecting to the foreign computer's client node
    serverNode = s.socket(s.AF_INET, s.SOCK_STREAM)
    serverNode.bind((HOST, PORT))
    serverNode.listen()
    remote, remote_address = serverNode.accept()
    remoteName = remote.recv(4096).decode()
    print("CONNECTED TO REMOTE: ", remoteName, "\nCOMMANDS: SENDFILE")
    
    # Receives data from foreign client
    try:
        while True:

            received = remote.recv(4096).decode()
            if received == "FILE":
                recvFile(remote, serverNode)

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



