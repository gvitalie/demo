import cv2

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
