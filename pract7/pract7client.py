import socket
import os

# Server IP address and port
HOST = '127.0.0.1'
PORT = 12345       

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Path to the video file to be sent
video_file_path = r'D:\sem_5_pracicles\cn_practical\pract7\dummy.mp4'

try:
    # Check if the video file exists
    if os.path.exists(video_file_path):
        # Send 'video' file type to the server first
        s.sendto(b'video', (HOST, PORT))
        print(f"Sending video file from {video_file_path}...")

        # Send the video file data in chunks
        with open(video_file_path, 'rb') as f:
            while True:
                data = f.read(128)  # Read data in chunks of 128 bytes
                if not data:
                    break  # Stop reading when no more data
                s.sendto(data, (HOST, PORT))  # Send the data
                print(f"Sent {len(data)} bytes.")  # Debug statement

        # Send 'EOF' to indicate the end of file
        s.sendto(b'EOF', (HOST, PORT))
        print("Video file has been sent successfully.")
    else:
        print(f"File not found at the specified path: {video_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the socket once the file is sent
s.close()
