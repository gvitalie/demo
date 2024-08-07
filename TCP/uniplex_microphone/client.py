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

latency = 'high'
# Audio receiving loop
try:
    with sd.OutputStream(samplerate=samplerate, channels=channels,
                         dtype=np.int16, latency=latency) as stream:
        socket_buffer = 128
        while True:
            audio_frame_size = int(client_socket.recv(socket_buffer).decode('utf-8'))

            acknowledge = 'OK'.encode('utf-8')
            client_socket.send(acknowledge)

            iterations = audio_frame_size//socket_buffer
            if audio_frame_size % socket_buffer > 0:
                iterations += 1

            audio_data_bytes = b''
            for i in range(iterations):
                audio_data_bytes += client_socket.recv(socket_buffer)  # Receive audio data from the server
                if not audio_data_bytes:
                    break

            acknowledge = 'OK'.encode('utf-8')
            client_socket.send(acknowledge)

            audio_data = np.frombuffer(audio_data_bytes, dtype=np.int16)  # Convert bytes to numpy array
            stream.write(audio_data)  # Play received audio data
except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"Error: {e}")

# Cleanup
print("Closing connection...")
client_socket.close()

