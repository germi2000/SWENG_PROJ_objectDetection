# Import library
import cv2
import datetime

from colorDetection import ColorDetector

# Class to edit the image
class Labeling:
    def __init__(self):
        self.color_detector = ColorDetector("config.conf")
        
    # Methode to put the text on the right place
    def label_shape(self, detected_shapes, image, contour, objectShape):
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            #detect color 
            color_name = self.color_detector.detect_color(image, cX, cY)

            cv2.putText(image, objectShape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(image, color_name, (cX - 15, cY - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            currentTime = datetime.datetime.now()
            if objectShape is not None and color_name is not None:
                detected_shapes.append([currentTime, objectShape, color_name])

        return detected_shapes

    # Methode to frame de contour
    def draw_contour(self, image, contour):
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

