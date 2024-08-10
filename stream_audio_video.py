import threading

import cv2
import sounddevice as sd


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


def microphone(event):
    with sd.Stream(channels=None, callback=callback, samplerate=8000) as stream:
        event.wait()


if __name__ == "__main__":

    microphone_event = threading.Event()
    microphone_thread = threading.Thread(target=microphone, args=(microphone_event,))
    microphone_thread.daemon = True
    microphone_thread.start()

    web_cam_video = cv2.VideoCapture(0)

    print("Streaming ...")
    try:
        while True:
            ret, frame = web_cam_video.read()

            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        print("\nVideo disconnected")
        web_cam_video.release()
        cv2.destroyAllWindows()