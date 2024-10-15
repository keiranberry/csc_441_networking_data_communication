# Import socket module
from socket import *
import sys  # In order to terminate the program

# Create a TCP server socket (AF_INET is used for IPv4 protocols and SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Socket setup: 
# Set port number, bind, and listen 

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print("The server is ready to receive on port:", serverPort)

while True:
    # Establish the connection
    print('Ready to serve...')
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()
    try:
        # Get the client request
        message = connectionSocket.recv(2048).decode()
        print("Message received from client:", message)

        # Parse the client's request and extract the requested filename
        filename = message.split()[1]  # First element is GET, second is the filename
        f = open(filename[1:])  # Open the file, ignoring the leading '/'

        # Read the content of the file
        outputdata = f.read()

        # Send an HTTP header line into the socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())


        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found (404)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())


        # Close the client socket
        connectionSocket.close()


serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
