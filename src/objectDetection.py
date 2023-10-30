import cv2
import numpy as np
from colorDetection import ColorDetector


class ShapeDetector:
    def __init__(self):
        self.color_detector = ColorDetector()

    def detect(self, image):

        # Kantenerkennung
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        
        # Konturen finden
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        detected_shapes = []

        for contour in contours:

            if cv2.contourArea(contour) < 40 * 40:
                continue
            elif cv2.contourArea(contour) > 400 * 400:
                continue
            
            # Initialize shape as "Unknown"
            shape = " "
            color_name = " "
            # Extract color from a 3x3 region around the centroid
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                color_name = self.color_detector.detect_color(image,cX,cY)

                # Kontur approximieren and detect shapes
                epsilon = 0.04 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
                num_sides = len(approx)

                # Formen erkennen und umrahmen
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

                # Beschriftung hinzufügen
                cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                cv2.putText(image, color_name, (cX - 15, cY - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            # Gefundene Formen speichern
            detected_shapes.append((shape, contour, color_name))

            # Umrahmung hinzufügen
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

        return image, detected_shapes
