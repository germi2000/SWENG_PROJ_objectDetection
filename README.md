# SWENG_PROJ_objectDetection
Detailed Documentation: Create documentation to guide users through your applications setup,
features, and usage. Please provide a meaningful runtime view diagram showing what your application
does. The documentation shall be a part of the repository.

# Live Object Pattern Recognition and Color Detection

# Overview
SWENG_PROJ_objectDetection is a small Python application that uses the livestream of a camera and performs real-time 
object pattern recognition and color detection. The recognition is visualized within the livestream and the 
information gathered is logged into a csv file for later analysis. 
The code is part of the module SoftwareEngineering at the University of Applied Sciences Grisogns.


# Setup
## Prerequisites
1. Python Enviroment on your Windows PC
2. Camera

## Installation
step-by-step instructions for installing SWENG_PROJ_objectDetection. 

1. clone the SWENG_PROJ_objectDetection repository  
```
git clone https://github.com/germi2000/SWENG_PROJ_objectDetection.git
```
3. setup the poetry venv  
```
poetry shell
```
4. select camera_index in the main.py file
```
# Camera init
    camera = Camera(camera_index=0)
```
5. start the main.py file

# Features
Describe the key features of your application. Each feature should have its own section.

## cameraCapture.py
A Class named Camera for capturing video frames from a camera using the OpenCV library. 
1. Initialization: Creates a camera instance based on the provided camera index (default is 0).
2. Error Handling: Raises an error if the camera cannot be opened.
3. Capture Frame: Captures and returns a video frame as a NumPy array.
4. Release: Provides a method to release the camera when no longer needed. Useful for freeing system resources.

## colorDetection.py
A Class named ColorDetector for detecting the color of a object in an image based on its 
HSV (Hue, Saturation, Value) values. The class has the following features:
1. Color Classification: Classify the HSV values of the colors: Red, Green, Blue, Yellow and Violet.
2. Detect Color: Given an image and pixel coordinates, it converts the image to HSV, extracts a small region around the pixel, calculates the average color, and classifies it.

## editImage.py
A class named Labeling for labeling shapes and their colors in an image. This class is intended for image processing and analysis and has the following features:
1. Label Shape: Labels detected shapes in images, calculating centroids and colors and adding text labels.
2. Draw Contour: Draws a contour around detected shapes in images.


# Usage
Provide detailed guidance on how to use your application.

## Getting Started
Give users a quick start guide to using your application. Include basic steps to get up and running.

Step 1: [Instruction]
Step 2: [Instruction]
Step 3: [Instruction]

## Example Use Case
Walk users through a real-world example of how your application can be used. Include screenshots or code snippets to illustrate.

Scenario: [Description]
Step 1: [Instruction]
Step 2: [Instruction]

# runtime view diagram
Create and include a meaningful runtime view diagram that visually represents how your application works. This diagram should show the different components, modules, or services of your application and how they interact with each other.

# Troubleshooting
Include a section for troubleshooting common issues users might encounter and solutions for resolving them.

# FAQ
Anticipate frequently asked questions and provide answers in this section.
