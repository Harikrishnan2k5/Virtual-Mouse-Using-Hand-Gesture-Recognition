import cv2
import mediapipe as mp
import pyautogui
import math

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    raise IOError("Cannot open webcam")


hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils


screen_width, screen_height = pyautogui.size()


margin = 0.05
click_threshold = 35

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape


    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark


            index_finger = landmarks[8]
            thumb_finger = landmarks[4]

            x_index = int(index_finger.x * frame_width)
            y_index = int(index_finger.y * frame_height)

            x_thumb = int(thumb_finger.x * frame_width)
            y_thumb = int(thumb_finger.y * frame_height)


            index_x = min(max(int(screen_width * (x_index / frame_width)), 0), screen_width-1)
            index_y = min(max(int(screen_height * ((y_index / frame_height)*(1+margin))), 0), screen_height-1)

            thumb_x = min(max(int(screen_width * (x_thumb / frame_width)), 0), screen_width-1)
            thumb_y = min(max(int(screen_height * ((y_thumb / frame_height)*(1+margin))), 0), screen_height-1)


            pyautogui.moveTo(index_x, index_y, duration=0.05)


            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            if distance < click_threshold:
                pyautogui.click()
                pyautogui.sleep(0.2)


            cv2.circle(frame, (x_index, y_index), 10, (0, 255, 255), cv2.FILLED)
            cv2.circle(frame, (x_thumb, y_thumb), 10, (0, 255, 255), cv2.FILLED)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
