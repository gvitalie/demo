import socket
import queue
import threading
import pickle
import cv2

SERVER = ('localhost', 3456)


def webcam_frame(clients):
    webcam_video = cv2.VideoCapture(0)
    webcam_video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    webcam_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
    print("WebCam streaming ...")

    try:
        while True:
            ret, frame = webcam_video.read()

            frame_data = pickle.dumps(frame)

            if clients:
                for client_id in clients:
                    if client_id[1].empty():
                        client_id[1].put(frame_data)
            else:
                break

    except Exception as e:
        print(e)
    finally:
        webcam_video.release()
        print('WebCam disconnected')


def client_frame(client_id, clients):
    while True:
        try:
            frame_data = client_id[1].get()
            frame_size = str(len(frame_data)).encode('utf-8')

            client_id[0][0].sendall(frame_size)
            acknowledge = client_id[0][0].recv(4094)

            client_id[0][0].sendall(frame_data)
            acknowledge = client_id[0][0].recv(4096)

            # print(acknowledge.decode('utf-8'))
        except Exception as e:
            clients.remove(client_id)
            print(e, f'-> Client {client_id[0][1]} disconnected')
            break


if __name__ == "__main__":
    with socket.socket() as server:
        try:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(SERVER)
            server.listen()
            print('Server listen\n')

            try:
                clients = list()
                while True:
                    client = server.accept()
                    client = (client, queue.Queue(1))
                    print(f'Client {client[0][1]} connected')

                    if not clients:
                        clients.append(client)
                        webcam_thread = threading.Thread(target=webcam_frame,
                                                         args=(clients,))
                        webcam_thread.daemon = True
                        webcam_thread.start()
                    else:
                        clients.append(client)

                    client_thread = threading.Thread(target=client_frame,
                                                     args=(client, clients))
                    client_thread.daemon = True
                    client_thread.start()
            except Exception as e:
                print(e)
        except KeyboardInterrupt:
            pass
        finally:
            print('\nServer down')
