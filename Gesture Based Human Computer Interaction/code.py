# import tkinter as tk
# import cv2
# import mediapipe as mp
# import pyautogui
# from PIL import Image
# import threading

# # Button 1: Hand-based volume control
# def button1_click():
#     def volume_control():
#         print('Button1 was Clicked')
#         x1 = y1 = x2 = y2 = 0
#         webcam = cv2.VideoCapture(0)
#         my_hands = mp.solutions.hands.Hands()
#         drawing_utils = mp.solutions.drawing_utils
        
#         while True:
#             _, image = webcam.read()
#             image = cv2.flip(image, 1)
#             frame_height, frame_width, _ = image.shape
#             rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             output = my_hands.process(rgb_image)
#             hands = output.multi_hand_landmarks
            
#             if hands:
#                 for hand in hands:
#                     drawing_utils.draw_landmarks(image, hand)
#                     landmarks = hand.landmark
#                     for id, landmark in enumerate(landmarks):
#                         x = int(landmark.x * frame_width)
#                         y = int(landmark.y * frame_height)
#                         if id == 8:
#                             cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
#                             x1 = x
#                             y1 = y
#                         if id == 4:
#                             cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
#                             x2 = x
#                             y2 = y
#                     dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
#                     cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
#                     if dist > 50:
#                         pyautogui.press("volumeup")
#                     else:
#                         pyautogui.press("volumedown")
            
#             cv2.imshow("Hand Volume Control", image)
#             key = cv2.waitKey(10)
#             if key == 27:
#                 break
        
#         webcam.release()
#         cv2.destroyAllWindows()

#     threading.Thread(target=volume_control).start()

# # Button 2: Virtual Mouse Control using hand gestures
# def button2_click():
#     def virtual_mouse():
#         print('Button2 was Clicked')
#         cap = cv2.VideoCapture(0)
#         hand_detector = mp.solutions.hands.Hands()
#         drawing_utils = mp.solutions.drawing_utils
#         screen_width, screen_height = pyautogui.size()
#         index_y = 0
        
#         while True:
#             _, frame = cap.read()
#             frame = cv2.flip(frame, 1)
#             frame_height, frame_width, _ = frame.shape
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             output = hand_detector.process(rgb_frame)
#             hands = output.multi_hand_landmarks
            
#             if hands:
#                 for hand in hands:
#                     drawing_utils.draw_landmarks(frame, hand)
#                     landmarks = hand.landmark
#                     for id, landmark in enumerate(landmarks):
#                         x = int(landmark.x * frame_width)
#                         y = int(landmark.y * frame_height)
#                         if id == 8:
#                             cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                             index_x = screen_width / frame_width * x
#                             index_y = screen_height / frame_height * y
#                             pyautogui.moveTo(index_x, index_y)
#                         if id == 4:
#                             cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                             thumb_x = screen_width / frame_width * x
#                             thumb_y = screen_height / frame_height * y
#                             if abs(index_y - thumb_y) < 50:
#                                 pyautogui.click()
#                                 pyautogui.sleep(1)
            
#             cv2.imshow('Virtual Mouse', frame)
#             key = cv2.waitKey(1)
#             if key == 27:
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

#     threading.Thread(target=virtual_mouse).start()

# # Button 3: Eye-controlled mouse
# def button3_click():
#     def eye_control():
#         cam = cv2.VideoCapture(0)
#         face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
#         screen_w, screen_h = pyautogui.size()
        
#         while True:
#             _, frame = cam.read()
#             frame = cv2.flip(frame, 1)
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             output = face_mesh.process(rgb_frame)
#             landmark_points = output.multi_face_landmarks
#             frame_h, frame_w, _ = frame.shape
            
#             if landmark_points:
#                 landmarks = landmark_points[0].landmark
#                 for id, landmark in enumerate(landmarks[474:478]):
#                     x = int(landmark.x * frame_w)
#                     y = int(landmark.y * frame_h)
#                     cv2.circle(frame, (x, y), 3, (0, 255, 0))
#                     if id == 1:
#                         screen_x = screen_w / frame_w * x
#                         screen_y = screen_h / frame_h * y
#                         pyautogui.moveTo(screen_x, screen_y)
#                 left = [landmarks[145], landmarks[159]]
#                 for landmark in left:
#                     x = int(landmark.x * frame_w)
#                     y = int(landmark.y * frame_h)
#                     cv2.circle(frame, (x, y), 3, (0, 255, 255))
#                 if (left[0].y - left[1].y) < 0.008:
#                     pyautogui.click()
#                     pyautogui.sleep(1)
        
#             cv2.imshow('Eye Controlled Mouse', frame)
#             key = cv2.waitKey(1)
#             if key == 27:
#                 break
        
#         cam.release()
#         cv2.destroyAllWindows()

#     threading.Thread(target=eye_control).start()

# # Button 4: Photo capture
# def button4_click():
#     def photo_capture():
#         cam = cv2.VideoCapture(0)
#         i = 0
#         _ = None
#         a = None
#         while True:
#             _, frame = cam.read()
#             cv2.imshow('frame', frame)
#             cv2.waitKey(10)
#             if i == 50:
#                 if _:
#                     cv2.imwrite('captured_photo.jpg', frame)  # Corrected the indentation here
#                     a = 'captured_photo.jpg'
#                     print("Photo captured and saved as 'captured_photo.jpg'")
#                 break
#             i += 1
        
#         cam.release()
#         cv2.destroyAllWindows()

#         if a:
#             image = Image.open(a)
#             image.show()

#     threading.Thread(target=photo_capture).start()

# # Setting up the tkinter window with buttons
# window = tk.Tk()
# window.title("Gesture-Based Controls")

# button1 = tk.Button(window, text="Hand Volume Control", command=button1_click)
# button1.pack(pady=5)

# button2 = tk.Button(window, text="Virtual Mouse Control", command=button2_click)
# button2.pack(pady=5)

# button3 = tk.Button(window, text="Eye-Controlled Mouse", command=button3_click)
# button3.pack(pady=5)

# button4 = tk.Button(window, text="Photo Capture", command=button4_click)
# button4.pack(pady=5)

# # Start the tkinter event loop
# window.mainloop()


import tkinter as tk
import cv2
import mediapipe as mp
import pyautogui
from PIL import Image
import threading
import subprocess

# Flags for controlling individual threads
stop_thread1 = False
stop_thread2 = False
stop_thread3 = False
stop_thread4 = False
stop_thread5 = False
stop_thread6 = False

# Button 1: Hand-based volume control
def button1_click():
    def volume_control():
        global stop_thread1
        stop_thread1 = False
        print('Button1 was Clicked')
        x1 = y1 = x2 = y2 = 0
        webcam = cv2.VideoCapture(0)
        my_hands = mp.solutions.hands.Hands()
        drawing_utils = mp.solutions.drawing_utils
        
        while not stop_thread1:
            _, image = webcam.read()
            if not _:
                break
            image = cv2.flip(image, 1)
            frame_height, frame_width, _ = image.shape
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            output = my_hands.process(rgb_image)
            hands = output.multi_hand_landmarks
            
            if hands:
                for hand in hands:
                    drawing_utils.draw_landmarks(image, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        if id == 8:
                            cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                            x1 = x
                            y1 = y
                        if id == 4:
                            cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                            x2 = x
                            y2 = y
                    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
                    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
                    if dist > 50:
                        pyautogui.press("volumeup")
                    else:
                        pyautogui.press("volumedown")
            
            cv2.imshow("Hand Volume Control", image)
            key = cv2.waitKey(10)
            if key == 27 or stop_thread1:
                break
        
        webcam.release()
        cv2.destroyAllWindows()

    # Start the volume control thread
    threading.Thread(target=volume_control).start()

# Button 2: Virtual Mouse Control using hand gestures
def button2_click():
    def virtual_mouse():
        global stop_thread2
        stop_thread2 = False
        print('Button2 was Clicked')
        cap = cv2.VideoCapture(0)
        hand_detector = mp.solutions.hands.Hands()
        drawing_utils = mp.solutions.drawing_utils
        screen_width, screen_height = pyautogui.size()
        index_y = 0
        
        while not stop_thread2:
            _, frame = cap.read()
            if not _:
                break
            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks
            
            if hands:
                for hand in hands:
                    drawing_utils.draw_landmarks(frame, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        if id == 8:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            index_x = screen_width / frame_width * x
                            index_y = screen_height / frame_height * y
                            pyautogui.moveTo(index_x, index_y)
                        if id == 4:
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            thumb_x = screen_width / frame_width * x
                            thumb_y = screen_height / frame_height * y
                            if abs(index_y - thumb_y) < 50:
                                pyautogui.click()
                                pyautogui.sleep(1)
            
            cv2.imshow('Virtual Mouse', frame)
            key = cv2.waitKey(1)
            if key == 27 or stop_thread2:
                break

        cap.release()
        cv2.destroyAllWindows()

    # Start the virtual mouse control thread
    threading.Thread(target=virtual_mouse).start()

# Button 3: Eye-controlled mouse
def button3_click():
    def eye_control():
        global stop_thread3
        stop_thread3 = False
        cam = cv2.VideoCapture(0)
        face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        screen_w, screen_h = pyautogui.size()
        
        while not stop_thread3:
            _, frame = cam.read()
            if not _:
                break
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = face_mesh.process(rgb_frame)
            landmark_points = output.multi_face_landmarks
            frame_h, frame_w, _ = frame.shape
            
            if landmark_points:
                landmarks = landmark_points[0].landmark
                for id, landmark in enumerate(landmarks[474:478]):
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0))
                    if id == 1:
                        screen_x = screen_w / frame_w * x
                        screen_y = screen_h / frame_h * y
                        pyautogui.moveTo(screen_x, screen_y)
                left = [landmarks[145], landmarks[159]]
                for landmark in left:
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 255))
                if (left[0].y - left[1].y) < 0.008:
                    pyautogui.click()
                    pyautogui.sleep(1)
        
            cv2.imshow('Eye Controlled Mouse', frame)
            key = cv2.waitKey(1)
            if key == 27 or stop_thread3:
                break
        
        cam.release()
        cv2.destroyAllWindows()

    threading.Thread(target=eye_control).start()

# Button 4: Photo capture
def button4_click():
    def photo_capture():
        global stop_thread4
        stop_thread4 = False
        cam = cv2.VideoCapture(0)
        i = 0
        a = None
        while not stop_thread4:
            _, frame = cam.read()
            if not _:
                break
            cv2.imshow('frame', frame)
            if i == 50:
                cv2.imwrite('captured_photo.jpg', frame)
                a = 'captured_photo.jpg'
                print("Photo captured and saved as 'captured_photo.jpg'")
                break
            i += 1
            cv2.waitKey(10)
        
        cam.release()
        cv2.destroyAllWindows()

        if a:
            image = Image.open(a)
            image.show()

    threading.Thread(target=photo_capture).start()

# Button 5: Open Calculator
def button5_click():
    subprocess.Popen("calc.exe")

# Button 6: Open Notepad
def button6_click():
    subprocess.Popen("notepad.exe")

# Function to stop only the running thread
def stop_current_thread(thread_name):
    global stop_thread1, stop_thread2, stop_thread3, stop_thread4, stop_thread5, stop_thread6
    if thread_name == "button1":
        stop_thread1 = True
    elif thread_name == "button2":
        stop_thread2 = True
    elif thread_name == "button3":
        stop_thread3 = True
    elif thread_name == "button4":
        stop_thread4 = True
    elif thread_name == "button5":
        stop_thread5 = True
    elif thread_name == "button6":
        stop_thread6 = True

# Setting up the tkinter window with buttons
window = tk.Tk()
window.title("Gesture-Based Controls")

# Create and style buttons
button1 = tk.Button(window, text="Hand Volume Control", command=button1_click, bg='lightblue')
button1.pack(pady=5)

button2 = tk.Button(window, text="Virtual Mouse Control", command=button2_click, bg='lightgreen')
button2.pack(pady=5)

button3 = tk.Button(window, text="Eye-Controlled Mouse", command=button3_click, bg='lightcoral')
button3.pack(pady=5)

button4 = tk.Button(window, text="Photo Capture", command=button4_click, bg='lightgoldenrod')
button4.pack(pady=5)

button5 = tk.Button(window, text="Open Calculator", command=button5_click, bg='lightpink')
button5.pack(pady=5)

button6 = tk.Button(window, text="Open Notepad", command=button6_click, bg='lightgray')
button6.pack(pady=5)

# No brightness buttons since brightness features were removed
# Stop button for each thread
stop_button1 = tk.Button(window, text="Stop Volume Control", command=lambda: stop_current_thread("button1"), bg='lightblue')
stop_button1.pack(pady=5)

stop_button2 = tk.Button(window, text="Stop Virtual Mouse", command=lambda: stop_current_thread("button2"), bg='lightgreen')
stop_button2.pack(pady=5)

stop_button3 = tk.Button(window, text="Stop Eye Mouse", command=lambda: stop_current_thread("button3"), bg='lightcoral')
stop_button3.pack(pady=5)

stop_button4 = tk.Button(window, text="Stop Photo Capture", command=lambda: stop_current_thread("button4"), bg='lightgoldenrod')
stop_button4.pack(pady=5)

stop_button5 = tk.Button(window, text="Stop Calculator", command=lambda: stop_current_thread("button5"), bg='lightpink')
stop_button5.pack(pady=5)

stop_button6 = tk.Button(window, text="Stop Notepad", command=lambda: stop_current_thread("button6"), bg='lightgray')
stop_button6.pack(pady=5)

# Start the tkinter event loop
window.mainloop()




