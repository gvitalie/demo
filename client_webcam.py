import socket
import cv2
import pickle
import struct


with socket.socket() as client:
    # print(client.getblocking())
    client.connect(("localhost", 3456))

    video = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = video.read()
            frame_data = pickle.dumps(frame)
            frame_data = struct.pack('Q', len(frame_data)) + frame_data

            client.sendall(frame_data)

            # recover = pickle.loads(frame_data)
            # print(recover)
            # cv2.imshow("Client", recover)

            cv2.imshow("Client", frame)
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        video.release()
        cv2.destroyAllWindows()
        print("\nClient disconnected")

