from socket import *
import ssl

# Create the client socket
clientSocket = socket(AF_INET,SOCK_STREAM)

# Wrap the socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem') # Load the server's certificate
clientSocket = context.wrap_socket(clientSocket,server_hostname='localhost')

# Connect to the server
clientSocket.connect(('localhost', 12345))

# Get user input
sentence = input('Input lowercase sentence:')

# Send a message
clientSocket.send(sentence.encode())

# Receive the response
modifiedSentence = clientSocket.recv(2048)

print('From Server: ', modifiedSentence.decode())

# Close the connection
clientSocket.close()