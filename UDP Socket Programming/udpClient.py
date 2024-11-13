# Part 2
# from socket import *
# # Destination Address
# destAddr = ('localhost', 12000)
# # Create UDP socket
# clientSocket = socket(AF_INET, SOCK_DGRAM)
# # Get user keyboard input
# message = input('Input lowercase sentence: ')
# # Send the keyboard input to server
# clientSocket.sendto(message.encode(), destAddr )
# # Receive server's response
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print(modifiedMessage.decode())
# clientSocket.close()

# Part 3
from socket import *
# Destination Address
destAddr = ('localhost', 12000)
# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # Get user keyboard input
    message = input('Client: ')
    
    # Send message to server
    clientSocket.sendto(message.encode(), destAddr)

    # Wait for a response from server
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    # Print message from server
    print('Server:', modifiedMessage.decode())