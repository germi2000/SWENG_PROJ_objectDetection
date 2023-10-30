
"""
Fachhochschule Graubünden

Klasse: MRVZ21
Fach: Software Engineering
Projektname: Object Detection

Autoren: Yannick Kohler, Tim Germann

Datum: 26.10.2023
Version: 1.0
"""


# Import library
import cv2
import csv
import datetime
# Import classes
from cameraCapture import Camera
from objectDetection import ShapeDetector

# Main programm
if __name__ == "__main__":

    # Set the right camera index

    camera = Camera(camera_index=0)
    try:
        while True:
            
            # Shows the raw camera feed
            frame = camera.capture_frame()
            cv2.imshow("Camera Capture", frame)

            # Detect Objects and edit the image
            shape_detector = ShapeDetector()
            result, detected_shapes = shape_detector.detect(frame)

            # Shows the edited camera feed
            cv2.imshow("Shape Detection", result)
                                    
            # Press key 'q' to quit the live camera feed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                # Dateiname für die CSV-Datei
                csv_filename = "detected_shapes.csv"

                #CSV-Datei im Schreibmodus öffnen
                with open(csv_filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
        
                    # Schreiben Sie die Überschriften (optional)
                    writer.writerow(["Timestamp","Pattern", "Color"])
        
                    # Schreiben Sie die Daten aus detected_shapes in die CSV-Datei
                    writer.writerows([detected_shapes[0], detected_shapes[1], detected_shapes[2]])

                print(f"Die Daten wurden in die Datei '{csv_filename}' geschrieben.")
                break

    except KeyboardInterrupt:
        print("Exiting the program.")

    camera.release()
    cv2.destroyAllWindows()