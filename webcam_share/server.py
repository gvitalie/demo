import socket
import pickle
import struct
import threading

import cv2


def send_webcam_frame(clients):
    web_cam_video = cv2.VideoCapture(0)
    print("Streaming WebCam share ...")
    try:
        while True:
            ret, frame = web_cam_video.read()
            frame_data = pickle.dumps(frame)
            frame_size = len(frame_data)
            frame_data = struct.pack('Q', frame_size) + frame_data

            if clients:
                for client_id in clients:
                    try:
                        client_id[0].send(frame_data)
                    except Exception as e:
                        print(e, f'-> Client {client[1][0]}:{client_id[1][1]} disconnected')
                        clients.remove(client_id)
            else:
                break

    except Exception as e:
        print(e)
    finally:
        print("WebCam disconnected\n")
        web_cam_video.release()


if __name__ == "__main__":
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('localhost', 3456))
        server.listen()
        print('Server listen\n')

        try:
            clients = list()
            while True:
                client = server.accept()
                print(client[1], 'connected')

                if not clients:
                    send_webcam_frame_thread = threading.Thread(target=send_webcam_frame,
                                                            args=[clients])
                    send_webcam_frame_thread.daemon = True
                    send_webcam_frame_thread.start()
                clients.append(client)

        except KeyboardInterrupt:
            print('\nServer down')
        finally:
            pass
