# Import library
import cv2

# Class to edit the image
class Labeling:
    
    # Methode to put the text on the right place
    def label_shape(self, image, contour, objectShape):
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(image, objectShape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Methode to save the shape
    def save_shape(self, detected_shapes, objectShape, contour):
        detected_shapes.append((objectShape, contour))

    # Methode to frame de contour
    def draw_contour(self, image, contour):
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)