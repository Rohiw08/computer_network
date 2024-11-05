#############################CLIENT.PY#############################

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=3528
host=socket.gethostbyname('localhost')
s.connect((host,port))
print(s.recv(1024).decode())
s.close()



