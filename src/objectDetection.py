# Import librarys
import cv2
import numpy as np

# Import class
from editImage import Labeling
from colorDetection import ColorDetector

# Define function identify and frame objects
def identify_shape(num_sides, contour):
    if num_sides == 3:
        shape = "Triangle"
    elif num_sides == 4:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h
        if 0.90 <= aspect_ratio <= 1.10:
            shape = "Square"
        else:
            shape = "Rectangle"
    elif 5 <= num_sides <= 8:
        shape = "Circle"
    else:
        shape = "N/A"
    return shape

# Class to detect contours and call edit images functions
class ShapeDetector:

    def __init__(self):
        self.labeling = Labeling()
        self.detected_shapes = []

    def detect(self, image):
        
        # Create grayscale for easier contour detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # detect contours
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)       

        for contour in contours:       
        
            # filter for the right size
            if cv2.contourArea(contour) < 40 * 40:
                continue
            elif cv2.contourArea(contour) > 400 * 400:
                continue

            # contour approximation
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            num_sides = len(approx)

            # Call function to identify and frame object
            objectShape = identify_shape(num_sides, contour)

            # Call methodes from Labeling class to edit image
            self.detected_shapes = self.labeling.label_shape(self.detected_shapes, image, contour, objectShape)
            self.labeling.draw_contour(image, contour)

        return image, self.detected_shapes
