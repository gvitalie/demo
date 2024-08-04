import socket
import struct
import pickle
import cv2


if __name__ == "__main__":
    with socket.socket() as client:
        client.connect(("localhost", 3456))
        client_ip, client_port = client.getsockname()
        print(f'Client {client_ip}:{client_port} connected')

        try:
            packets = b''
            frame_size = 0
            frame_index_size = struct.calcsize('Q')
            while True:
                packet = client.recv(4096)
                packets += packet
                if not packet:
                    print(client.getpeername(), 'disconnected')
                    break
                if not frame_size:
                    frame_size = struct.unpack('Q', packets[:frame_index_size])[0]
                    packets = packets[frame_index_size:]
                if len(packets) > frame_size:
                    frame_data = packets[:frame_size]
                    packets = packets[frame_size:]
                    frame_size = 0

                    frame = pickle.loads(frame_data)
                    cv2.imshow(f'{client_ip}:{client_port}', frame)
                    key = cv2.waitKey(1) == ord('q')
                    if key:
                        break

        except KeyboardInterrupt:
            pass
        finally:
            print(f'\nClient {client_ip}:{client_port} disconnected')
            cv2.destroyAllWindows()
