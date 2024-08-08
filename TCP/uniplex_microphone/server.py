import socket
import sounddevice as sd
import numpy as np

# Socket setup
HOST = 'localhost'  # Replace with your server IP or 'localhost'
PORT = 12345         # Choose a port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# Accept a client connection
client_socket, addr = server_socket.accept()
print(f"Accepted connection from {addr}")

# Audio setup
samplerate = 44100
channels = 1

print("Streaming audio...")

latency = 'low'
# Audio streaming loop
try:
    with sd.InputStream(samplerate=samplerate, channels=channels,
                        dtype=np.int16, latency=latency) as stream:
        while True:
            audio_data, _ = stream.read(1024)  # Read audio data from the microphone
            client_socket.sendall(audio_data.tobytes())  # Send audio data to the client
except Exception as e:
    print(f"Error: {e}")

# Cleanup
print("Closing connections...")
client_socket.close()
server_socket.close()

