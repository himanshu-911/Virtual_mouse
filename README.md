
# Virtual mouse

#### AI powered mouse which moves along with the movement of index finger and also clicks when index and middle fingers are brought together.

## Here are  the libraries and modules used in the video:

- **OpenCV**: an open-source library for computer vision
- **MediaPipe**: an open-source framework for building multimedia processing pipelines
- **AutoPy**: a Python library for automating mouse and keyboard actions


## Here are the steps involved in creating an the virtual mouse using OpenCV, NumPy, MediaPipe, and autopy:

- Find the hand landmarks.
- Get the tip of the index and middle fingers.
- Check which fingers are up.
- Check if it is in moving mode (only index finger up).
- Convert the hand coordinates to screen coordinates.
- Smoothen the hand movements.
- Move the mouse.
- Check if it is in clicking mode (both index and middle fingers up).
- Find the distance between the index and middle fingers.
- Click the mouse if the distance is short.
- Calculate the frame rate.
- Display the hand landmarks and bounding box.
