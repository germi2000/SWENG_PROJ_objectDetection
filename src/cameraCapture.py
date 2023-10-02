import cv2

def capture_camera(camera_index=1):
    # Open the camera using the specified camera_index (default is 0 for the default camera)
    cap = cv2.VideoCapture(camera_index)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # Capture a frame from the camera
            ret, frame = cap.read()

            # Check if the frame was captured successfully
            if not ret:
                print("Error: Could not read a frame.")
                break

            # Display the captured frame
            cv2.imshow("Camera Capture", frame)

            # Exit the loop if the user presses the 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_camera()
