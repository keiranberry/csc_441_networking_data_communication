from socket import *
# Server's address and port number
serverName = 'localhost' #hostname or IP address
serverPort = 12000

# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiate 3-way handshake
# When successful, a TCP connection is established
clientSocket.connect( (serverName,serverPort) )

# Get user input
sentence = input('Input lowercase sentence:')

# Drop message into TCP connection
clientSocket.send(sentence.encode())
# Compare with UDP Client's
# clientSocket.sento(sentence.encode(), (serverName, serverPort))

# Receive server's reply from TCP connection
modifiedSentence = clientSocket.recv(2048)
print('From Server: ', modifiedSentence.decode())

# Closes the socket and, hence, close the TCP connection
clientSocket.close()