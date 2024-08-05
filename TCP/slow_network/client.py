import socket
from time import sleep
import struct
import pickle
import cv2

SERVER = ('localhost', 3456)


def recv_frame(client):
    packets = b''
    frame_size = 0
    frame_index_size = struct.calcsize('Q')
    while True:
        packet = client.recv(4096)
        packets += packet
        if not frame_size:
            frame_size = struct.unpack('Q', packets[:frame_index_size])[0]
            packets = packets[frame_index_size:]
        if len(packets) == frame_size:
            frame_data = packets[:frame_size]
            packets = b''
            frame_size = 0

            # Uncomment to simulate slow network
            # sleep(0.2)

            client.send('OK'.encode('utf-8'))

            frame = pickle.loads(frame_data)
            cv2.imshow(f'{client.getsockname()}', frame)
            key = cv2.waitKey(1) == ord('q')
            if key:
                break


if __name__ == "__main__":
    with socket.socket() as client:
        client.connect(SERVER)
        print(f'Client {client.getsockname()} connected')

        try:
            recv_frame(client)
        except KeyboardInterrupt:
            pass
        finally:
            print(f'\nClient {client.getsockname()} disconnected')