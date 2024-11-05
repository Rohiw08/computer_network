############################CLIENT.PY########################

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msgFromClient = "Message for UDP server from UDP client"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 30945)
bufferSize = 1024
sock.sendto(bytesToSend, serverAddressPort)

msgFromServer = sock.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0].decode())
print(msg)