import socket
import sounddevice as sd
import numpy as np
import pickle

# Socket setup
HOST = 'localhost'  # Replace with your server IP or 'localhost'
PORT = 12345         # Choose a port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# Accept a client connection
client_socket, addr = server_socket.accept()
print(f"Accepted connection from {addr}")

# Audio setup
samplerate = 15000
channels = 1

print("Streaming audio...")

latency = 'high'
# Audio streaming loop
try:
    with sd.InputStream() as stream:

        socket_buffer = 1024
        while True:
            audio_data, _ = stream.read(stream.read_available)  # Read audio data from the microphone
            # audio_frame = audio_data.tobytes()
            audio_frame = pickle.dumps(audio_data)
            audio_frame_size = len(audio_frame)

            client_socket.send(str(audio_frame_size).encode('utf-8'))
            acknowledge = client_socket.recv(socket_buffer)

            client_socket.sendall(audio_frame)  # Send audio data to the client
            acknowledge = client_socket.recv(socket_buffer)
except Exception as e:
    print(f"Error: {e}")

# Cleanup
print("Closing connections...")
client_socket.close()
server_socket.close()
