#############################CLIENT.PY#############################

import socket

HOST = '127.0.0.1'  
PORT = 3333  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    while True:
        message = input("Enter your message: ")  # Get user input
        s.sendall(message.encode())  # Send the message to the server

        if message == 'stop':  # Break if 'stop' message is sent
            print("Stopping the client...")
            break

        data = s.recv(1024).decode()  # Receive data from the server
        print('Server says:', data)  # Print the server's response


