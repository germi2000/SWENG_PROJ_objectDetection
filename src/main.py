import cv2

from cameraCapture import Camera

if __name__ == "__main__":
    camera = Camera(camera_index=1)

    try:
        while True:
            frame = camera.capture_frame()
            cv2.imshow("Camera Capture", frame)





            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Exiting the program.")

    camera.release()
    cv2.destroyAllWindows()
