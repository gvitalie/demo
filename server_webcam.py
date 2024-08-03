import socket
import struct
import pickle
import cv2


with socket.socket() as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # print(server.getblocking())
    server.bind(("localhost", 3456))
    server.listen()

    try:
        client, address = server.accept()
        print(address, 'connected')

        packets = b''
        frame_size = b''
        payload_size = struct.calcsize('Q')
        while True:
            for i in range(20):
                packet = client.recv(4096)
                packets += packet
            if not packet:
                break
            if not frame_size:
                frame_size = packets[:payload_size]
                frame_size_int = struct.unpack('Q', frame_size)[0]
                # print(frame_size_int)
                packets = packets[payload_size:]
            if len(packets) > frame_size_int:
                frame_data = packets[:frame_size_int]
                packets = packets[frame_size_int:]
                frame_size = b''

                frame = pickle.loads(frame_data)
                cv2.imshow('Server', frame)
                key = cv2.waitKey(1) == ord('q')
                if key:
                    break

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        print("\nServer down")
