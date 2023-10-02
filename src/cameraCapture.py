import cv2

class Camera:
    def __init__(self, camera_index=1):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise ValueError("Error: Could not open camera.")

    def capture_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            raise ValueError("Error: Could not read a frame.")

        return frame

    def release(self):
        self.cap.release()

