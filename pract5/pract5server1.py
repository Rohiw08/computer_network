######UDP#######

#############################SERVER.PY#############################

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Successfully created")
port=3528
host=socket.gethostbyname('localhost')

s.bind((host,port))
print("Socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr=s.accept()
    print("Got connection from ",addr)
    c.send("Thank you for connecting".encode())
    c.close()
    break


