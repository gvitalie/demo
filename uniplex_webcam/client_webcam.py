import socket
import cv2
import pickle
import struct


with socket.socket() as client:
    client.connect(("localhost", 3456))
    print('Client connected\n')

    web_cam_video = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = web_cam_video.read()
            frame_data = pickle.dumps(frame)
            frame_size = len(frame_data)
            frame_data = struct.pack('Q', frame_size) + frame_data

            try:
                client.sendall(frame_data)
            except Exception as e:
                print('\n', e, '-> Server or network may be down')
                break

            cv2.imshow("Client", frame)
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        print("\nClient disconnected")
    finally:
        web_cam_video.release()
        cv2.destroyAllWindows()

