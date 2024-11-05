####TCP####

############################SERVER.PY#############################

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
localip='127.0.0.1'
localport=30945
buffersize=1024
message="Message for UDP client from UDP server"
encode=message.encode()

sock.bind((localip,localport))
print("UDP server up and listening")
while(True):
    bytesAddressPair = sock.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client: {}".format(message.decode())
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    sock.sendto(encode, address)
    break


