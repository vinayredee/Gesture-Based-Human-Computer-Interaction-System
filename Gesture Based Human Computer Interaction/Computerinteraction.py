# import tkinter as tk
# import cv2
# import mediapipe as mp
# import pyautogui
# from PIL import Image
# def button1_click():
#     print('Button1 was Clicked')
#     x1=y1=x2=y2=0
#     webcam=cv2.VideoCapture(0)
#     my_hands=mp.solutions.hands.Hands()
#     drawing_utils=mp.solutions.drawing_utils
#     while True:
#         _,image=webcam.read()
#         image=cv2.flip(image,1)
#         frame_height,frame_width,_ =image.shape
#         rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#         output=my_hands.process(rgb_image)
#         hands=output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(image,hand)
#                 landmarks=hand.landmark
#                 for id,landmark in enumerate(landmarks):
#                     x=int(landmark.x*frame_width)
#                     y=int(landmark.y*frame_height)
#                     if id==8:
#                         cv2.circle(img=image,center=(x,y),radius=8,color=(0,255,255),thickness=3)
#                         x1=x
#                         y1=y
#                     if id==4:
#                         cv2.circle(img=image,center=(x,y),radius=8,color=(0,0,255),thickness=3)
#                         x2=x
#                         y2=y
#             dist=((x2-x1)**2+(y2-y1)**2)**(0.5)//4
#             cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)
#             if dist>50:
#                 pyautogui.press("volumeup")
#             else:
#                 pyautogui.press("volumedown")
#         cv2.imshow("Hand volume control using python done by Rahil",image)
#         key=cv2.waitKey(10)
#         if key==27:
#             break
#     webcam.release()
#     cv2.destroyAllWindows()
# def button2_click():
#     print('Button2 was Clicked')
#     cap=cv2.VideoCapture(0)
#     hand_detector=mp.solutions.hands.Hands()
#     drawing_utils=mp.solutions.drawing_utils
#     screen_width,screen_height=pyautogui.size()
#     index_y=0
#     while True:
#         _, frame=cap.read()
#         frame=cv2.flip(frame,1)
#         frame_height,frame_width,_=frame.shape
#         rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         output=hand_detector.process(rgb_frame)
#         hands=output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(frame,hand)
#                 landmarks=hand.landmark
#                 for id,landmark in enumerate(landmarks):
#                     x=int(landmark.x*frame_width)
#                     y=int(landmark.y*frame_height)
#                     print(x,y)
#                     if id==8:
#                         cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
#                         index_x=screen_width/frame_width*x
#                         index_y=screen_height/frame_height*y
#                         pyautogui.moveTo(index_x,index_y)
#                     if id==4:
#                         cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
#                         thumb_x=screen_width/frame_width*x
#                         thumb_y=screen_height/frame_height*y
#                         print(abs(index_y-thumb_y))
#                         if abs(index_y-thumb_y)<50:
#                             pyautogui.click()
#                             pyautogui.sleep(1)
#         cv2.imshow('Virtual Mouse',frame)
#         cv2.waitKey(1)
# def button3_click():
#     cam=cv2.VideoCapture(0)
#     face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
#     screen_w,screen_h=pyautogui.size()
#     while True:
#         _, frame=cam.read()
#         frame=cv2.flip(frame,1)
#         rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         output=face_mesh.process(rgb_frame)
#         landmark_points=output.multi_face_landmarks
#         frame_h,frame_w,_=frame.shape
#         if landmark_points:
#             landmarks=landmark_points[0].landmark
#             for id,landmark in enumerate(landmarks[474:478]):
#                 x=int(landmark.x*frame_w)
#                 y=int(landmark.y*frame_h)
#                 cv2.circle(frame,(x,y),3,(0,255,0))
#                 if id==1:
#                     screen_x=screen_w/frame_w*x
#                     screen_y=screen_h/frame_h*y
#                     pyautogui.moveTo(screen_x,screen_y)
#                 left=[landmarks[145],landmarks[159]]
#                 for landmark in left:
#                     x=int(landmark.x*frame_w)
#                     y=int(landmark.y*frame_h)
#                     cv2.circle(frame,(x,y),3,(0,255,255))
#                 if (left[0].y-left[1].y)<0.008:
#                     pyautogui.click()
#                     pyautogui.sleep(1)
#         cv2.imshow('Eye Controlled Mouse',frame)
#         cv2.waitKey(1)
# def button4_click():
#     cam=cv2.VideoCapture(0)
#     i=0
#     _=None
#     a=None
#     while True:
#         _,frame=cam.read()
#         cv2.imshow('frame',frame)
#         cv2.waitKey(10)
#         if i==50:
#             if _:
#                 cv2.imwrite('captured_photo.jpg',frame)
#                 a='captured_photo.jpg'
#                 print("Photo captured and saved as 'captured_photo.jpg'")
#             break
#         i+=1
#     cam.release()
#     cv2.destroyAllWindows()
#     image=Image.open(a)
#     image.show()       
# window=tk.Tk()
# window.title("Button Example")
# button1=tk.Button(window,text="Button 1",command=button1_click)
# button1.pack()
# button2=tk.Button(window,text="Button 2",command=button2_click)
# button2.pack()
# button3=tk.Button(window,text="Button 3",command=button3_click)
# button3.pack()
# button4=tk.Button(window,text="Button 4",command=button4_click)
# button4.pack()
