import cv2

if __name__ == "__main__":
    image_frame = cv2.imread('Philosophy.png')

    print("Streaming ...")
    try:
        while True:
            frame = image_frame

            cv2.imshow('Philosophy', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        print("\nVideo disconnected")
        cv2.destroyAllWindows()
