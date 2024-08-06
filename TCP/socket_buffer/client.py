import queue
import socket
import pickle
import threading
import queue
import cv2
from time import sleep

SERVER = ('localhost', 3456)


def get_frame(client_id, queue_in, status):
    print('Get frames started')
    while not status.is_set():
        packet = client_id.recv(4096)
        frame_size = int(packet.decode('utf-8'))

        acknowledge = 'OK'.encode('utf-8')
        client_id.send(acknowledge)

        packets = b''
        for i in range(1 + frame_size//4096):
            packets += client_id.recv(4096)
        queue_in.put(packets)


def show_frame(client_id, queue_out, status):
    print('Show frames started')
    while not status.is_set():
        packets = queue_out.get()

        acknowledge = 'OK'.encode('utf-8')
        client_id.send(acknowledge)

        frame = pickle.loads(packets)

        cv2.imshow('Client', frame)
        key = cv2.waitKey(1) == ord('q')
        if key:
            status.set()
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    with socket.socket() as client:
        client.connect(SERVER)
        print(f'Client {client.getsockname()} connected\n')

        try:
            queue_link = queue.Queue()
            status = threading.Event()

            get_frame_thread = threading.Thread(target=get_frame,
                                                args=(client, queue_link, status,))
            # get_frame_thread.daemon = True
            get_frame_thread.start()
            # get_frame_thread.join()

            show_frame_thread = threading.Thread(target=show_frame,
                                                 args=(client, queue_link, status,))
            # show_frame_thread.daemon = True
            show_frame_thread.start()
            # get_frame_thread.join()

            while status.wait():
                break

        except KeyboardInterrupt:
            status.set()
            print(f'\nClient {client.getsockname()} disconnected')

