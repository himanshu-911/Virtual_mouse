import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

smoothing=2.7

plocX, plocY=0,0

clocX, clocY=0,0

index_y = 0
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width,_ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            
            for id, landmark in enumerate(landmarks):
                
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                
                if id == 8:
                    
                    cv2.circle(frame, (x,y), 10, (0, 255, 255), cv2.FILLED)
                    
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    clocX = plocX + (index_x - plocX) / smoothing
                    clocY = plocY + (index_y - plocY) / smoothing
                    
                    pyautogui.moveTo(clocX, clocY)
                    plocX, plocY = clocX, clocY
                if id == 12:
                    cv2.circle(frame, (x,y), 10, (0, 255, 255), cv2.FILLED)
                    middle_x = screen_width/frame_width*x
                    middle_y = screen_height/frame_height*y
                    print('Position', abs(index_y - middle_y))
                    
                    if abs(index_y - middle_y) < 50:
                        print('Click!')
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
