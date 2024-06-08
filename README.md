# Overview

This program is a simple peer-to-peer file sharer. Once the two computers are connected (w/ hardcoded IP's), string messages can be sent back and forth and files can be sent to a predetermined directory. 

I made this program to learn more about networking and file storage/manipulation in general. 


[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This program is a simple Peer-to-Peer network, meaning that both devices running the script are clients and servers and there is no central database/processor.

TCP and port #60001 was used. The scripts allows for simple string messages to be passed back and forth, as well as .txt files, .docx files, .jpg files, and any text file that can be encoded using base64.

# Development Environment

This project was made using Visual Studio Community Edition (2022) in Python.
Libraries used:
* Socket (IP connections over wireless network)
* Threading (Parallel processes)
* Base64 (Encoding data to and from binary)


# Useful Websites

* [File Transfer w/ TCP Socket Python (geeksforgeeks)](https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python/)
* [P2P Data Exchange (linkedin)](https://www.linkedin.com/pulse/implementing-peer-to-peer-data-exchange-inpython-luis-soares-m-sc-/)
* [Saving Files from Python (stackoverflow)](https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac)
* [base64 Encoding (stackoverflow)](https://stackoverflow.com/questions/3715493/encoding-an-image-file-with-base64)

# Future Work

* Create a GUI
	* Make the textbox in the GUI dynamically save and shift unsent messages so incoming messages don't interrupt typing in the command prompt
* Make program detect file type
* Make basic antivirus file scanner
* Make P2P network larger
* Allow for several small packets to be sent, rather than one large packet which is very network-inefficient
* Make IP's and directories dynamic and not hard-coded