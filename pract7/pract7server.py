import socket
import subprocess
import os

# Server IP address and port
HOST = '127.0.0.1'
PORT = 12345       

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
try:
    s.bind((HOST, PORT))
    print(f"Server is listening on {HOST}:{PORT}...")
except Exception as e:
    print(f"Error binding the socket: {e}")
    s.close()
    exit()

BUFFER_SIZE = 65535  # Maximum size for a UDP packet
video_file_path = "received_video.mp4"  # File path where the video will be saved

while True:
    print("Waiting for a new video file...")

    # Receive file type or exit command
    try:
        file_type, addr = s.recvfrom(BUFFER_SIZE)
        file_type = file_type.decode().strip()  # Decode and clean the received file type
        print(f"Received file type: {file_type} from {addr}")
    except Exception as e:
        print(f"Error receiving file type: {e}")
        continue

    # Check if the client sent the "exit" command
    if file_type.lower() == "exit":
        print("Exit command received. Shutting down the server.")
        break  # Exit the loop to close the server

    # Ensure the received file is a video file
    if file_type.lower() == 'video':
        print(f"Receiving a video file from {addr}...")

        # Open the file to write binary data
        try:
            with open(video_file_path, 'wb') as f:
                while True:
                    data, addr = s.recvfrom(BUFFER_SIZE)  # Receive file data
                    if data == b'EOF':  # End of file indicator
                        print(f"Video file has been received and saved as '{video_file_path}'.")
                        break  # Break when the entire file is received
                    f.write(data)  # Write the received data to the file
        except Exception as e:
            print(f"Error writing file: {e}")
            continue

        # Play the received video using the default media player
        try:
            print("Playing the video...")
            # Open the video in the default media player and wait for it to close
            if os.name == 'nt':  # If the operating system is Windows
                subprocess.run(['start', video_file_path], shell=True)
            else:  # For Linux or macOS
                subprocess.run(['open', video_file_path] if os.name == 'posix' else ['xdg-open', video_file_path])
        except Exception as e:
            print(f"Error opening the video: {e}")

        # Terminate the server once the video is closed
        print("Video closed. Shutting down the server.")
        break  # Exit the loop to close the server
    else:
        print("Invalid file type received. Only video files are accepted.")

# Close the socket after the exit command
s.close()
print("Server has been closed.")
