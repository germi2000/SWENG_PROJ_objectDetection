
"""
Fachhochschule Graubünden

Class:          MRVZ21
Subject:        Software Engineering
Project name:   Object Detection

Authors:        Yannick Kohler, Tim Germann

Date:           01.11.2023
Version:        1.0
"""


# Import library
import cv2

# Import classes
from cameraCapture import Camera
from objectDetection import ShapeDetector
from logger import Logger
from selectableROI import ROISelector

# Main programm
if __name__ == "__main__":

    # Class init
    shape_detector = ShapeDetector()
    logger = Logger()
    roiselector = ROISelector()
    # Camera init
    camera = Camera(camera_index=2)

    # Create an open-cv window, for ROI selection
    cv2.namedWindow('Live Webcam')
    cv2.setMouseCallback('Live Webcam', roiselector.draw_rectangle)

    # Loop
    try:
        while True:
            
            # Shows the raw camera feed
            frame = camera.capture_frame()
            cv2.imshow("Live Webcam", frame)

            # Create a ROI camera feed
            img_roi = roiselector.output_roi(frame)
            
            # Detect Objects and shows the camera feed with shape detection
            result, detected_shapes = shape_detector.detect(img_roi)
            cv2.imshow("Shape Detection", result)
            
            # Press key 'q' to quit the live camera feed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logger.write_data(detected_shapes)
                break

    except KeyboardInterrupt:
        print("Exiting the program.")

    # Close all Windows
    camera.release()
    cv2.destroyAllWindows()