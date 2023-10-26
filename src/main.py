import cv2

from cameraCapture import Camera
from objectDetection import ShapeDetector

if __name__ == "__main__":
    camera = Camera(camera_index=0)

    try:
        while True:
            frame = camera.capture_frame()
            cv2.imshow("Camera Capture", frame)

          # ShapeDetector-Objekt erstellen und Formen erkennen
            shape_detector = ShapeDetector()
            result, detected_shapes = shape_detector.detect(frame)

            # Livebild anzeigen
            cv2.imshow("Shape Detection", result)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Exiting the program.")

    camera.release()
    cv2.destroyAllWindows()