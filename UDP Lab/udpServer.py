# Part 2
# from socket import *
# # Server's port number
# serverPort = 12000
# # Create UDP socket
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# # Explicitly assign port number to server’s socket
# serverSocket.bind(('localhost', serverPort))
# print('The server is ready to receive...')
# while True:
#     # Waits for a packet to arrive
#     message, clientAddress = serverSocket.recvfrom(2048)
#     # Manipulate client message
#     modifiedMessage = message.decode().replace('o', 'i')
#     # Send reply to client
#     serverSocket.sendto(modifiedMessage.encode(), clientAddress)

# Part 3
from socket import *
# Server's port number
serverPort = 12000
# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Explicitly assign port number to server’s socket
serverSocket.bind(('localhost', serverPort))
print('The server is ready to receive...')

while True:
    # Wait for a packet to arrive
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # Manipulate client message
    modifiedMessage = message.decode()
    
    # Print message from client
    print('Client:', modifiedMessage)
    
    # Get user keyboard input
    reply = input('Server: ')
    
    # Send reply to client
    serverSocket.sendto(reply.encode(), clientAddress)
