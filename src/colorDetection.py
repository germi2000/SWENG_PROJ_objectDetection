import cv2
import numpy as np

class ColorDetector:
    def __init__(self):
        pass

    def classify_color(self, average_hsv_color):
        # Define HSV color ranges for red, green, blue, yellow, and violet
        color_ranges = {
            "Red": (np.array([0, 50, 50]), np.array([10, 255, 255])),
            "Green": (np.array([35, 50, 50]), np.array([85, 255, 255])),
            "Blue": (np.array([100, 50, 50]), np.array([130, 255, 255])),
            "Yellow": (np.array([20, 50, 50]), np.array([30, 255, 255])),
            "Violet": (np.array([130, 50, 50]), np.array([160, 255, 255]))
        }

        for color_name, (lower, upper) in color_ranges.items():
            if np.all(average_hsv_color >= lower) and np.all(average_hsv_color <= upper):
                return color_name

        return "Unknown"
    
    def detect_color(self, image, cX, cY):
        
         # Convert the image to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Extract color from a 3x3 region around the centroid (cX, cY)
        color_region = hsv[cY - 1:cY + 2, cX - 1:cX + 2]

        # Calculate the average HSV color in the region
        average_hsv_color = np.mean(color_region, axis=(0, 1)).astype(int)

        # Classify the color using the ColorDetector class
        color_name = self.classify_color(average_hsv_color)

        return color_name