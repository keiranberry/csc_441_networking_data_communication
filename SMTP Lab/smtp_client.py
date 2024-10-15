from socket import *

msg = "\r\n Winners never quit. Quitters never quit. Don't give up!"
endmsg = "\r\n.\r\n"

# Choose a mail server and call it mailserver
mailserver = ('localhost', 1025)


# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO sdsmt.edu\r\n'
print('C:', heloCommand)
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM:<keiran.berry@mines.sdsmt.edu>\r\n'
print('C:', mailFromCommand)
clientSocket.send(mailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
mailToCommand = 'RCPT TO:<oliver.schwab@mines.sdsmt.edu>\r\n'
print('C:', mailToCommand)
clientSocket.send(mailToCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
print('C:', dataCommand)
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)


# Send message header.
messageHeader = 'From: Keiran Berry <keiran.berry@mines.sdsmt.edu>\r\nTo: Oliver Schwab <oliver.schwab@mines.sdsmt.edu>\r\nSubject: SMTP Email!\r\n\r\n'
print('C:', messageHeader)
clientSocket.send(messageHeader.encode())

# Send message body.
print('C:', msg)
clientSocket.send(msg.encode())


# Message ends with a single period.
print('C:', endmsg)
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send QUIT command and get server response.
quitCommand = 'QUIT'
print('C:', quitCommand)
clientSocket.send(quitCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.close()