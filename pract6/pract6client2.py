import socket

# Server address (localhost) and port number
host = "127.0.0.1"
port = 12000

buffer_size = 1024

file_name = r"D:/sem_5_pracicles/cn_practical/Myfilenew.txt"  

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open(file_name, "rb") as f: 

    data = f.read(buffer_size)

    while data:
        sock.sendto(data, (host, port))

        data = f.read(buffer_size)

    sock.sendto("Now".encode(), (host, port))

# Close the socket
sock.close()

print("File sent successfully!")