🖱️ Virtual Mouse Using Hand Gesture Recognition (Click Control)
📘 Overview

This project demonstrates how a webcam can be used to control mouse movement and perform click actions using simple hand gestures.
It uses computer vision and machine learning-based landmark detection (MediaPipe) to track finger movements and translate them into cursor and click operations — without needing a physical mouse.

🚀 Features

✅ Real-time cursor movement using index finger.
✅ Left-click action when the thumb and index finger come close together.
✅ Fully works with just a webcam — no sensors required.
✅ Lightweight and efficient; runs on CPU.
✅ Simple, intuitive, and interactive human–computer interface.

🧠 Technologies Used
Library	Purpose
OpenCV	Captures real-time video frames and processes them for gesture detection.
MediaPipe	Detects and tracks 21 hand landmarks using machine learning models.
PyAutoGUI	Simulates mouse movement and click operations on the screen.
Math (Python)	Used to calculate the Euclidean distance between finger coordinates.
⚙️ How It Works

Camera Capture (OpenCV)
The webcam captures live frames and mirrors them for natural interaction.

Hand Landmark Detection (MediaPipe)
MediaPipe’s pre-trained ML model identifies 21 key points of the hand.

Cursor Movement
The index finger’s position is mapped to the screen coordinates using proportional scaling.

Click Detection
The distance between the thumb tip (Landmark 4) and index finger tip (Landmark 8) is calculated.

If the distance is less than a defined threshold → click action is triggered using pyautogui.click().

Visual Feedback
Circles are drawn on the fingertips to show tracking accuracy.

🧩 Code Structure
VirtualMouse/
│
├── code.py             # Main project file
├── requirements.txt    # Library dependencies
└── README.md           # Project documentation

🧑‍💻 Developed By

Hari Krishnan M
B.Tech in Computer Science and Engineering
Lovely Professional University, Jalandhar, India
📧 hari16krishna2k5@gmail.com

👩‍🏫 Guided by: Ms. Deepali Kumari, Assistant Professor

🧠 Core Concept: Where ML is Used

The MediaPipe Hands API uses a pre-trained deep learning model to:

Detect hands in the camera feed.

Identify 21 hand landmarks (like fingertips, joints, etc.) in real-time.

Provide landmark coordinates (x, y, z), which are used for gesture recognition.

So even though you didn’t train the ML model yourself, you’re using Google’s ML-based detection engine in your project — that’s where the machine learning part is applied!

🏁 Future Enhancements

💡 Add right-click and scroll gestures.
🎯 Smoothen pointer movement with Kalman filtering.
🚀 Enable multiple-hand gesture support for more interactions.
