import cv2
import numpy as np
import configparser

class ColorDetector:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        

    def classify_color(self, average_hsv_color):
        color_ranges = {}
        for color_name in self.config['ColorRanges']:
            range_str = self.config['ColorRanges'][color_name]
            lower_hsv, upper_hsv = map(int, range_str.split())
            color_ranges[color_name] = (np.array(lower_hsv), np.array(upper_hsv))

        for color_name, (lower, upper) in color_ranges.items():
            if np.all(average_hsv_color >= lower) and np.all(average_hsv_color <= upper):
                return color_name

        return "N/A"
    
    def detect_color(self, image, cX, cY):
        
        # Convert the image to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Extract color from a 5x5 region around the centroid (cX, cY)
        color_region = hsv[cY - 5:cY + 5, cX - 5:cX + 5]

        # Calculate the average HSV color in the region
        average_hsv_color = np.mean(color_region, axis=(0, 1)).astype(int)

        # Classify the color using the ColorDetector class
        color_name = self.classify_color(average_hsv_color)

        return color_name