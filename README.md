# Ball Tracking using OpenCV
```
# Object Tracking with OpenCV

This project demonstrates object tracking using color detection and the Hough Circle Transform in OpenCV. The tracked object is identified based on its color, and the path of the detected circles is drawn on the video feed.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Numpy

## Installation

To install the required libraries, you can use `pip`:

```sh
pip install opencv-python numpy
```

## Usage

1. **Set Up the Webcam:**

   Ensure you have a working webcam. The script uses the default camera (usually the built-in webcam) by setting `webcam = cv.VideoCapture(0)`.

2. **Select the Object Color:**

   The script starts by loading an image to select the color of the object to track. Make sure to replace the `image_path` variable with the path to your image:

   ```python
   image_path = 'path_to_your_image.jpg'
   ```

   When the script is run, it will display the image, and you can click on the object to select its color.

3. **Adjust the Thresholds:**

   Use the trackbars to adjust the HSV color thresholds for better detection of the object. The trackbars are created for adjusting the lower and upper bounds of the Hue (H), Saturation (S), and Value (V) channels.

4. **Run the Script:**

   Run the script and observe the webcam feed. The object within the specified color range will be tracked, and its path will be drawn on the video feed.

   ```sh
   python object_tracking.py
   ```

   Press `ESC` to exit the video feed.

## Code Explanation

- **Webcam Setup:**

  ```python
  webcam = cv.VideoCapture(0)
  webcam.set(3, frameWidth)
  webcam.set(4, frameHeight)
  webcam.set(10, 150)
  ```

- **Mouse Callback:**

  The `on_mouse` function captures the HSV color of the pixel where the mouse is clicked.

  ```python
  def on_mouse(event, x, y, flags, params):
      global ball_color_hsv
      if event == cv.EVENT_LBUTTONDOWN:
          ball_color_hsv = np.array(params[y, x])
          print("Selected HSV color:", ball_color_hsv)
  ```

- **Trackbars:**

  Trackbars are created to adjust the HSV thresholds.

  ```python
  cv.createTrackbar("H Lower", "Thresholds", 0, 179, nothing)
  cv.createTrackbar("H Upper", "Thresholds", 179, 179, nothing)
  cv.createTrackbar("S Lower", "Thresholds", 0, 255, nothing)
  cv.createTrackbar("S Upper", "Thresholds", 255, 255, nothing)
  cv.createTrackbar("V Lower", "Thresholds", 0, 255, nothing)
  cv.createTrackbar("V Upper", "Thresholds", 255, 255, nothing)
  ```

- **Circle Detection:**

  The `HoughCircles` function is used to detect circles in the thresholded image.

  ```python
  circles = cv.HoughCircles(frame_bin, cv.HOUGH_GRADIENT, 2, 10, param1=100, param2=40, minRadius=20, maxRadius=200)
  ```

- **Object Tracking:**

  Detected circles' centers are used to update the tracked objects' paths.

  ```python
  for obj in tracked_objects:
      for i in range(1, len(obj.centers)):
          if obj.centers[i - 1] is None or obj.centers[i] is None:
              continue
          if time.time() - obj.timestamps[i - 1] >= 1:  # 1-second delay
              cv.line(frame, obj.centers[i - 1], obj.centers[i], (0, 0, 255), 2)
  ```

## Acknowledgments

Special thanks to the OpenCV community for their extensive documentation and examples.
```
```