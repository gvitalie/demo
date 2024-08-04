import socket
import struct
import pickle
import cv2


with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 3456))
    server.listen()
    print('Server listening\n')

    try:
        client, address = server.accept()
        print(address, 'connected')

        packets = b''
        frame_size = 0
        frame_index_size = struct.calcsize('Q')
        while True:
            for i in range(111):
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
                cv2.imshow('Server', frame)
                key = cv2.waitKey(1) == ord('q')
                if key:
                    break

    except KeyboardInterrupt:
        print("\nServer down")
    finally:
        cv2.destroyAllWindows()
