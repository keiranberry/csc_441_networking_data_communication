from socket import *
import ssl
serverPort = 12345

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)

# Wrap the socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
serverSocket = context.wrap_socket(serverSocket, server_side=True)

print("Server listening on port 12345...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    # Receive data from the client
    sentence = connectionSocket.recv(2048)
    print(f"Received: { sentence.decode()}")

    capitalizedSentence = sentence.decode().upper()

    # Send a response
    connectionSocket.send(capitalizedSentence.encode())

    # Close the connection
    connectionSocket.close()