
# Virtual mouse

#### AI powered mouse which moves along with the movement of index finger and also clicks when index and middle fingers are brought together.




## Approach:
- Import **OpenCV** and **Mediapipe** libraries.
- Video from webcam is captured using **cv2.VideoCapture(0)** method.
- Using Mediapipe library, inbuilt **hands** method is used and **hand_detector** variable is created.
- Other inbuilt method, **drawing_utils** is used and **display_marks** variable is defined to display the detected       landmarks in the output video.
- Get the screen size you are working on using **pyautogui.size()**.
- Smoothen the movement of cursor.
- Then run an infinite loop.
- Extract the frames of the video using **read()** method and also flip the video.
- Convert default BGR format to RGB using **cv2.cvtColor()** method.
- Then process the RGB frames and detect landmarks using inbuilt **multi_hand_landmarks** method.
- Now to draw hand landmarks, use **display_marks** variable that we have created earlier.
- Get the positon of landmarks on x and y axis of the frame.
- Marking circle on the tip of index and middle finger.
- Calibratihg indices to move cursor on whole screen.
- Move the cursor along with the movement of index finger using **pyautogui.moveTo()**.
- If absolute distance between tip of index and middle finger is less than 50 pixels then it is considered as click.
- Use **pyautogui.click()** for click operation and after a click. 
- At the end, display the frames using the **cv2.imshow()** method.  
