from socket import *

# Set port number
serverPort = 12000

# Create "welcoming" socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Explicitly assign port number to socket
serverSocket.bind(('',serverPort))

# Wait and listen for some client to knock
serverSocket.listen(1)

print('The server is ready to receive...')

while True:
    # Welcome and create new dedicated socket
    connectionSocket, addr = serverSocket.accept()

    # Receive client's message from TCP connection
    sentence = connectionSocket.recv(2048)

    capitalizedSentence = sentence.decode().upper()

    # Send reply
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()