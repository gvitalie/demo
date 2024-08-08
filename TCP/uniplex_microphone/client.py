import socket
import sounddevice as sd
import numpy as np

# Socket setup
HOST = 'localhost'  # Replace with your server IP or 'localhost'
PORT = 12345         # The same port number used on the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Audio setup
samplerate = 44100
channels = 1

print("Receiving audio...")

latency = 'low'
# Audio receiving loop
try:
    with sd.OutputStream(samplerate=samplerate, channels=channels,
                         dtype=np.int16, latency=latency) as stream:
        while True:
            audio_data_bytes = client_socket.recv(1024)  # Receive audio data from the server
            if not audio_data_bytes:
                break
            audio_data = np.frombuffer(audio_data_bytes, dtype=np.int16)  # Convert bytes to numpy array
            stream.write(audio_data)  # Play received audio data
except Exception as e:
    print(f"Error: {e}")

# Cleanup
print("Closing connection...")
client_socket.close()

