import cv2
import numpy as np

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, image):
        # Grayscale-Bild erstellen
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Kantenerkennung
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        
        # Konturen finden
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        detected_shapes = []

        for contour in contours:
            # Kontur approximieren
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
            else:
                shape = "Unknown"

            # Beschriftung hinzufügen
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Gefundene Formen speichern
            detected_shapes.append((shape, contour))

            # Umrahmung hinzufügen
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

        return image, detected_shapes
