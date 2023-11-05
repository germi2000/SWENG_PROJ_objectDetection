# Import library
import cv2
import numpy as np

# Class to Select a region of interest
class ROISelector:
    def __init__(self):
        # Create a empty image
        self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        # Init mouse
        self.drawing = False
        self.ix, self.iy = -1, -1
        self.roi = None

    # mouseclick callback funktion
    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.roi = (self.ix, self.iy, x - self.ix, y - self.iy)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False

    def output_roi(self, frame):
        if self.roi is not None:
            x, y, w, h = self.roi
            # Cut roi
            roi_image = frame[y:y+h, x:x+w]
            # Create new roi image
            return roi_image
        else:
            return frame

