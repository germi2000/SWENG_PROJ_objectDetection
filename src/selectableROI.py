# Import library
import cv2
import numpy as np

class ROISelector:
    def __init__(self):
        # Erstellen Sie ein leeres Bild (Canvas) für die Auswahl
        self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        # Initialisieren Sie die Mausvariablen
        self.drawing = False
        self.ix, self.iy = -1, -1
        self.roi = None

    # Mausklick-Callback-Funktion
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
            # Schneiden Sie den ausgewählten ROI aus dem Livebild
            roi_image = frame[y:y+h, x:x+w]
            # Erstellen Sie ein neues Fenster für den ausgewählten ROI
            return roi_image
        else:
            return frame

