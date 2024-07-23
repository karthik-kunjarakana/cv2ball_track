#!/usr/bin/env python
import cv2 as cv
import numpy as np
import time

# Setup for object tracking
frameWidth = 640
frameHeight = 480
webcam = cv.VideoCapture(0)  # Use 0 for default camera
webcam.set(3, frameWidth)
webcam.set(4, frameHeight)
webcam.set(10, 150)  # Set brightness
cv.namedWindow("Camera", cv.WINDOW_AUTOSIZE)
ball_color_hsv = None

# To store the path of the detected circles
tracked_objects = []

class TrackedObject:
    def __init__(self, center):
        self.centers = [center]
        self.timestamps = [time.time()]

    def update(self, center):
        self.centers.append(center)
        self.timestamps.append(time.time())

def on_mouse(event, x, y, flags, params):
    global ball_color_hsv
    if event == cv.EVENT_LBUTTONDOWN:
        ball_color_hsv = np.array(params[y, x])
        print("Selected HSV color:", ball_color_hsv)

def nothing(x):
    pass

# Create trackbars for color change
cv.namedWindow("Thresholds")
cv.createTrackbar("H Lower", "Thresholds", 0, 179, nothing)
cv.createTrackbar("H Upper", "Thresholds", 179, 179, nothing)
cv.createTrackbar("S Lower", "Thresholds", 0, 255, nothing)
cv.createTrackbar("S Upper", "Thresholds", 255, 255, nothing)
cv.createTrackbar("V Lower", "Thresholds", 0, 255, nothing)
cv.createTrackbar("V Upper", "Thresholds", 255, 255, nothing)

# Load a frame to select the color
image_path = 'cv2ball_track/projectile_motion-master/my_image.jpg '  # Replace with your image path
frame = cv.imread(image_path)
if frame is None:
    print(f"Could not open or find the image: {image_path}")
    exit(0)

# Show the frame to select the color
frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
cv.imshow("Select Color", frame)
cv.setMouseCallback("Select Color", on_mouse, frame_hsv)
cv.waitKey(0)
cv.destroyWindow("Select Color")

if ball_color_hsv is not None:
    while True:
        h_lower = cv.getTrackbarPos("H Lower", "Thresholds")
        h_upper = cv.getTrackbarPos("H Upper", "Thresholds")
        s_lower = cv.getTrackbarPos("S Lower", "Thresholds")
        s_upper = cv.getTrackbarPos("S Upper", "Thresholds")
        v_lower = cv.getTrackbarPos("V Lower", "Thresholds")
        v_upper = cv.getTrackbarPos("V Upper", "Thresholds")

        lowerB = np.array([h_lower, s_lower, v_lower])
        upperB = np.array([h_upper, s_upper, v_upper])

        r, frame = webcam.read()
        if not r:
            print("Failed to grab frame")
            break
        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        frame_bin = cv.inRange(frame_hsv, lowerB, upperB)
        frame_bin = cv.GaussianBlur(frame_bin, (15, 15), 0)

        # Use the correct constant for the HoughCircles function
        circles = cv.HoughCircles(frame_bin, cv.HOUGH_GRADIENT, 2, 10,
                                  param1=100, param2=40, minRadius=20, maxRadius=200)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            detected_centers = [(c[0], c[1]) for c in circles[0, :]]

            # Update tracked objects with detected centers
            for center in detected_centers:
                matched = False
                for obj in tracked_objects:
                    if np.linalg.norm(np.array(center) - np.array(obj.centers[-1])) < 50:
                        obj.update(center)
                        matched = True
                        break
                if not matched:
                    tracked_objects.append(TrackedObject(center))

        # Draw the path of each tracked object
        for obj in tracked_objects:
            for i in range(1, len(obj.centers)):
                if obj.centers[i - 1] is None or obj.centers[i] is None:
                    continue
                if time.time() - obj.timestamps[i - 1] >= 1:  # 1-second delay
                    cv.line(frame, obj.centers[i - 1], obj.centers[i], (0, 0, 255), 2)

        cv.imshow("Camera", frame)
        cv.imshow("Thresholded", frame_bin)
        if cv.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
            break

# Clean up
webcam.release()
cv.destroyAllWindows()
