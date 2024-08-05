import socket
import threading
import pickle
import struct
import cv2
from queue import Queue

SERVER = ('localhost', 3456)


def webcam_frame(clients):
    web_cam_video = cv2.VideoCapture(0)
    print("WebCam streaming ...")
    try:
        while True:
            ret, frame = web_cam_video.read()
            frame_data = pickle.dumps(frame)
            frame_size = len(frame_data)
            frame_data = struct.pack('Q', frame_size) + frame_data

            if clients:
                for client_id in clients:
                    if client_id[1].empty():
                        client_id[1].put(frame_data)
            else:
                break

    except Exception as e:
        print(e)
    finally:
        print("WebCam disconnected")
        web_cam_video.release()


def client_webcam(client, clients):
    print(f'Client {client[0][1]} webcam_frame')
    while True:
        try:
            message = client[1].get()
            client[0][0].sendall(message)
            acknowledge = client[0][0].recv(4096)
        except Exception as e:
            clients.remove(client)
            print(e, f'-> Client {client[0][1]} disconnected')
            break
        # print(acknowledge.decode('utf-8'))


if __name__ == "__main__":
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(SERVER)
        server.listen()
        print('Server listen\n')

        try:
            clients = list()
            while True:
                client = server.accept()
                client = (client, Queue(1))
                print(f'Client {client[0][1]} connected')

                if not clients:
                    clients.append(client)
                    send_webcam_frame_thread = threading.Thread(target=webcam_frame,
                                                            args=(clients,))
                    send_webcam_frame_thread.daemon = True
                    send_webcam_frame_thread.start()
                else:
                    clients.append(client)

                client_thread = threading.Thread(target=client_webcam,
                                                 args=(client, clients,))
                # client_thread.daemon = True
                client_thread.start()

        except KeyboardInterrupt:
            pass
        finally:
            print('\nServer down')
