import socket
import pickle
import cv2
from time import sleep

SERVER = ('localhost', 3456)


if __name__ == "__main__":
    with socket.socket() as client:
        try:
            client.connect(SERVER)
            print(f'Client {client.getsockname()} connected')

            try:
                print('Get frames')
                while True:
                    packet = client.recv(4096)
                    if not packet:
                        break
                    frame_size = int(packet.decode('utf-8'))

                    acknowledge = 'OK'.encode('utf-8')
                    client.send(acknowledge)

                    packets = b''
                    iterations = frame_size//4096
                    if frame_size % 4096 > 0:
                        iterations += 1
                    for i in range(iterations):
                        packets += client.recv(4096)

                    # Uncomment to simulate slow network
                    # sleep(0.2)

                    acknowledge = 'OK'.encode('utf-8')
                    client.send(acknowledge)

                    frame = pickle.loads(packets)

                    cv2.imshow(f'Client {client.getsockname()}', frame)
                    key = cv2.waitKey(1) == ord('q')
                    if key:
                        break

            except KeyboardInterrupt:
                pass
            finally:
                print(f'\nClient {client.getsockname()} disconnected')
                cv2.destroyAllWindows()
        except Exception as e:
            print('\n', e, "-> Server or network may be down")
