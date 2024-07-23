# # #!/usr/bin/env python
# # import cv2
# # import numpy as np

# # # Setup
# # webcam = cv2.VideoCapture()
# # cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)
# # ball_color_hsv = None

# # def on_mouse(event, x, y, flags, params):
# #     if event == cv2.EVENT_LBUTTONDOWN:
# #         global ball_color_hsv
# #         ball_color_hsv = np.array(frame_hsv[y, x])
# #         print(ball_color_hsv)

# # # Grab a frame
# # while True:
# #     r, frame = webcam.read()
# #     frame = cv2.GaussianBlur(frame, (15, 15), 0)  # Corrected GaussianBlur
# #     cv2.imshow("Camera", frame)
# #     if cv2.waitKey(1) != -1:
# #         break

# # # Get average color of selected area
# # cv2.imshow("Camera", frame)
# # frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# # cv2.setMouseCallback("Camera", on_mouse)
# # cv2.waitKey(0)

# # threshold = np.array([0.10, 0.20, 0.30])
# # difference = np.multiply(ball_color_hsv, threshold)
# # lowerB = np.subtract(ball_color_hsv, difference)
# # upperB = np.add(ball_color_hsv, difference)

# # while True:
# #     r, frame = webcam.read()
# #     frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# #     frame_bin = cv2.inRange(frame_hsv, lowerB, upperB)
# #     frame_bin = cv2.GaussianBlur(frame_bin, (15, 15), 0)  # Corrected GaussianBlur

# #     # Use the correct constant for the HoughCircles function
# #     circles = cv2.HoughCircles(frame_bin, cv2.HOUGH_GRADIENT, 2, 10,
# #                                param1=100, param2=40, minRadius=20, maxRadius=200)
    
# #     if circles is not None:
# #         circles = np.uint16(np.around(circles))
# #         for c in circles[0, :]:
# #             center = (c[0], c[1])
# #             radius = c[2]
# #             cv2.circle(frame, center, radius, (0, 255, 0), 1)
# #             cv2.circle(frame, center, 2, (0, 0, 255), 3)

# #     cv2.imshow("Camera", frame)
# #     if cv2.waitKey(1) != -1:
# #         break

# # # Clean Up
# # webcam.release()
# # cv2.destroyAllWindows()




# #!/usr/bin/env python
# import cv2
# import numpy as np

# # Setup
# webcam = cv2.VideoCapture(0)  # Use 0 for default camera or provide a video file path
# cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)
# ball_color_hsv = None

# def on_mouse(event, x, y, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         global ball_color_hsv
#         ball_color_hsv = np.array(frame_hsv[y, x])
#         print(ball_color_hsv)

# # Grab a frame
# while True:
#     r, frame = webcam.read()
#     if not r:
#         print("Failed to grab frame")
#         break
#     frame = cv2.GaussianBlur(frame, (15, 15), 0)  # Corrected GaussianBlur
#     cv2.imshow("Camera", frame)
#     if cv2.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
#         break

# # Get average color of selected area
# cv2.imshow("Camera", frame)
# frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# cv2.setMouseCallback("Camera", on_mouse)
# cv2.waitKey(0)

# # Ensure ball_color_hsv is not None before proceeding
# if ball_color_hsv is not None:
#     threshold = np.array([0.10, 0.20, 0.30])
#     difference = np.multiply(ball_color_hsv, threshold)
#     lowerB = np.subtract(ball_color_hsv, difference)
#     upperB = np.add(ball_color_hsv, difference)

#     while True:
#         r, frame = webcam.read()
#         if not r:
#             print("Failed to grab frame")
#             break
#         frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         frame_bin = cv2.inRange(frame_hsv, lowerB, upperB)
#         frame_bin = cv2.GaussianBlur(frame_bin, (15, 15), 0)  # Corrected GaussianBlur

#         # Use the correct constant for the HoughCircles function
#         circles = cv2.HoughCircles(frame_bin, cv2.HOUGH_GRADIENT, 2, 10,
#                                    param1=100, param2=40, minRadius=20, maxRadius=200)

#         if circles is not None:
#             circles = np.uint16(np.around(circles))
#             # Find the circle with the largest radius (assuming it's the most perfect)
#             largest_circle = max(circles[0, :], key=lambda c: c[2])
#             center = (largest_circle[0], largest_circle[1])
#             radius = largest_circle[2]
#             cv2.circle(frame, center, radius, (0, 255, 0), 1)
#             cv2.circle(frame, center, 2, (0, 0, 255), 3)

#         cv2.imshow("Camera", frame)
#         if cv2.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
#             break

# # Clean Up
# webcam.release()
# cv2.destroyAllWindows()
#!/usr/bin/env python
# import cv2
# import numpy as np

# # Setup
# frameWidth = 640
# frameHeight = 480
# webcam = cv2.VideoCapture(0)  # Use 0 for default camera
# webcam.set(3, frameWidth)
# webcam.set(4, frameHeight)
# webcam.set(10, 150)  # Set brightness
# cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)
# ball_color_hsv = None

# # To store the path of the detected circles
# circle_centers = []

# def on_mouse(event, x, y, flags, params):
#     global ball_color_hsv
#     if event == cv2.EVENT_LBUTTONDOWN:
#         ball_color_hsv = np.array(frame_hsv[y, x])
#         print("Selected HSV color:", ball_color_hsv)

# # Grab a frame to select the color
# while True:
#     r, frame = webcam.read()
#     if not r:
#         print("Failed to grab frame")
#         break
#     frame = cv2.GaussianBlur(frame, (15, 15), 0)
#     cv2.imshow("Camera", frame)
#     if cv2.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
#         break

# # Get the average color of the selected area
# cv2.imshow("Camera", frame)
# frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# cv2.setMouseCallback("Camera", on_mouse)
# cv2.waitKey(0)

# if ball_color_hsv is not None:
#     threshold = np.array([10, 40, 40])  # Adjust thresholds for better detection
#     difference = np.multiply(ball_color_hsv, threshold / 255.0)
#     lowerB = np.subtract(ball_color_hsv, difference)
#     upperB = np.add(ball_color_hsv, difference)

#     while True:
#         r, frame = webcam.read()
#         if not r:
#             print("Failed to grab frame")
#             break
#         frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         frame_bin = cv2.inRange(frame_hsv, lowerB, upperB)
#         frame_bin = cv2.GaussianBlur(frame_bin, (15, 15), 0)

#         # Use the correct constant for the HoughCircles function
#         circles = cv2.HoughCircles(frame_bin, cv2.HOUGH_GRADIENT, 2, 10,
#                                    param1=100, param2=40, minRadius=20, maxRadius=200)

#         if circles is not None:
#             circles = np.uint16(np.around(circles))
#             # Find the circle with the largest radius
#             largest_circle = max(circles[0, :], key=lambda c: c[2])
#             center = (largest_circle[0], largest_circle[1])
#             radius = largest_circle[2]
#             cv2.circle(frame, center, radius, (0, 255, 0), 1)
#             cv2.circle(frame, center, 2, (0, 0, 255), 3)
#             # Append the center to the list of circle centers
#             circle_centers.append(center)

#         # Draw the path of the circles
#         for i in range(1, len(circle_centers)):
#             if circle_centers[i - 1] is None or circle_centers[i] is None:
#                 continue
#             cv2.line(frame, circle_centers[i - 1], circle_centers[i], (0, 0, 255), 2)

#         cv2.imshow("Camera", frame)
#         if cv2.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
#             break

# # Clean up
# webcam.release()
# cv2.destroyAllWindows()
#!/usr/bin/env python
import cv2
import numpy as np

# Setup
frameWidth = 640
frameHeight = 480
webcam = cv2.VideoCapture(0)  # Use 0 for default camera
webcam.set(3, frameWidth)
webcam.set(4, frameHeight)
webcam.set(10, 150)  # Set brightness
cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)
ball_color_hsv = None

# To store the path of the detected circles
circle_centers = []

def on_mouse(event, x, y, flags, params):
    global ball_color_hsv
    if event == cv2.EVENT_LBUTTONDOWN:
        ball_color_hsv = np.array(frame_hsv[y, x])
        print("Selected HSV color:", ball_color_hsv)

def nothing(x):
    pass

# Create trackbars for color change
cv2.namedWindow("Thresholds")
cv2.createTrackbar("H Lower", "Thresholds", 0, 179, nothing)
cv2.createTrackbar("H Upper", "Thresholds", 0, 179, nothing)
cv2.createTrackbar("S Lower", "Thresholds", 0, 255, nothing)
cv2.createTrackbar("S Upper", "Thresholds", 0, 255, nothing)
cv2.createTrackbar("V Lower", "Thresholds", 0, 255, nothing)
cv2.createTrackbar("V Upper", "Thresholds", 0, 255, nothing)

# Set default values for the trackbars
cv2.setTrackbarPos("H Lower", "Thresholds", 0)
cv2.setTrackbarPos("H Upper", "Thresholds", 179)
cv2.setTrackbarPos("S Lower", "Thresholds", 0)
cv2.setTrackbarPos("S Upper", "Thresholds", 255)
cv2.setTrackbarPos("V Lower", "Thresholds", 0)
cv2.setTrackbarPos("V Upper", "Thresholds", 255)

# Grab a frame to select the color
while True:
    r, frame = webcam.read()
    if not r:
        print("Failed to grab frame")
        break
    frame = cv2.GaussianBlur(frame, (15, 15), 0)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
        break

# Get the average color of the selected area
cv2.imshow("Camera", frame)
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.setMouseCallback("Camera", on_mouse)
cv2.waitKey(0)

if ball_color_hsv is not None:
    while True:
        h_lower = cv2.getTrackbarPos("H Lower", "Thresholds")
        h_upper = cv2.getTrackbarPos("H Upper", "Thresholds")
        s_lower = cv2.getTrackbarPos("S Lower", "Thresholds")
        s_upper = cv2.getTrackbarPos("S Upper", "Thresholds")
        v_lower = cv2.getTrackbarPos("V Lower", "Thresholds")
        v_upper = cv2.getTrackbarPos("V Upper", "Thresholds")

        lowerB = np.array([h_lower, s_lower, v_lower])
        upperB = np.array([h_upper, s_upper, v_upper])

        r, frame = webcam.read()
        if not r:
            print("Failed to grab frame")
            break
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_bin = cv2.inRange(frame_hsv, lowerB, upperB)
        frame_bin = cv2.GaussianBlur(frame_bin, (15, 15), 0)

        # Use the correct constant for the HoughCircles function
        circles = cv2.HoughCircles(frame_bin, cv2.HOUGH_GRADIENT, 2, 10,
                                   param1=100, param2=40, minRadius=20, maxRadius=200)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            # Find the circle with the largest radius
            largest_circle = max(circles[0, :], key=lambda c: c[2])
            center = (largest_circle[0], largest_circle[1])
            radius = largest_circle[2]
            cv2.circle(frame, center, radius, (0, 255, 0), 1)
            cv2.circle(frame, center, 2, (0, 0, 255), 3)
            # Append the center to the list of circle centers
            circle_centers.append(center)

        # Draw the path of the circles
        for i in range(1, len(circle_centers)):
            if circle_centers[i - 1] is None or circle_centers[i] is None:
                continue
            cv2.line(frame, circle_centers[i - 1], circle_centers[i], (0, 0, 255), 2)

        cv2.imshow("Camera", frame)
        cv2.imshow("Thresholded", frame_bin)
        if cv2.waitKey(1) & 0xFF == 27:  # Exit if ESC key is pressed
            break

# Clean up
webcam.release()
cv2.destroyAllWindows()
