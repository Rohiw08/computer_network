import socket

# Server address (localhost) and port number
host = "127.0.0.1"
port = 12000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified address and port
sock.bind((host, port))


with open(r'D:/sem_5_pracicles/cn_practical/Myfilenew.txt', 'wb') as f:
    print('New file created in D:\\sem_5_pracicles\\cn_practical')

    data, addr = sock.recvfrom(1024)

    while data:
        
        print(data)

        if data.decode("utf-8") == "Now":
            break

        
        f.write(data)
        data, addr = sock.recvfrom(1024)

    print('File is successfully received!!!')

with open(r'D:/sem_5_pracicles/cn_practical/Myfilenew.txt', 'r') as f:
    print(f.read())  

# Close the socket
sock.close()

print('Connection closed!')