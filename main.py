import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
eye_closed = False
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points =output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]): # enumerate will generate id
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0)) #show landmarks
            if id == 1:
                screen_x = int(screen_w * (x / frame_w))
                screen_y = int(screen_h * (y / frame_h))
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]] # upper and bottom left eye's coordinate
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                if not eye_closed:
                    pyautogui.click()
                    eye_closed = True
            else:
                eye_closed = False
    cv2.imshow('Eye controlled mouse', frame)
    cv2.waitKey(10) # delay


