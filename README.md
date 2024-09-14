-- Gesture-Based Human-Computer Interaction System

This project demonstrates a gesture-based control system using hand gestures, eye movement, and photo capture via a webcam. It uses Python, OpenCV, MediaPipe, and PyAutoGUI to enable interaction with the system without the need for traditional input devices like a mouse or keyboard.

Features
Hand-Based Volume Control:-

Control your system's volume by moving your thumb and index finger closer or farther apart.
Hand landmarks are detected using MediaPipe, and volume is adjusted based on the distance between the landmarks.

Virtual Mouse Control using Hand Gestures:-

Control your system's mouse using hand movements.
Move the index finger to control the cursor position and click using thumb proximity detection.

Eye-Controlled Mouse:-

Move the mouse cursor with your eye movement.
Left-click with a blink detected via MediaPipe's face mesh landmarks.

Photo Capture:-

Capture a photo from your webcam after 50 frames and display the captured image.
Technologies Used

Tkinter: For creating the GUI with buttons to control each feature.
OpenCV: For capturing video frames from the webcam and processing them.
MediaPipe: For hand and face detection and landmark identification.
PyAutoGUI: For automating system-level controls like mouse movements, clicks, and volume control.
Pillow (PIL): For handling and displaying the captured photo.

Controls
Hand Volume Control: Adjust the volume by moving your hand (thumb and index finger).
Virtual Mouse Control: Move the mouse with your hand. Click by bringing your index finger close to your thumb.
Eye-Controlled Mouse: Move the mouse with your eye. Click by blinking.
Photo Capture: Click the button to capture a photo after 50 frames and display it.
Stop Buttons
Each feature has a corresponding "Stop" button to stop the ongoing process. Click the stop button to terminate the running thread for that specific feature.

Dependencies
Python 3.6 or higher
OpenCV
MediaPipe
PyAutoGUI
Pillow
Future Enhancements
Add gesture recognition for more system controls (e.g., play/pause music, next/previous slide).
Improve eye-tracking accuracy for more refined control.
Add support for more hand gestures.
License
This project is licensed under the MIT License.

Feel free to modify it according to your specific needs. You can add additional sections such as "Known Issues" or "Troubleshooting" if needed!






