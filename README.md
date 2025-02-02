# Eye Controlled Mouse

## Description

This project enables hands-free mouse control using eye tracking. It utilizes OpenCV, MediaPipe, and PyAutoGUI to track eye movement and control the cursor position accordingly. A blink gesture can be used to simulate a mouse click.

## Features

- Tracks eye movement to move the mouse cursor
- Detects eye blinking to trigger mouse clicks
- Uses real-time face landmark detection with MediaPipe Face Mesh


## Usage

1. Start the script, and the webcam will activate.
2. Move your eyes to control the cursor position.
3. Blink to perform a mouse click.
4. Stop the running code to exit.

## How It Works

- The script captures frames from the webcam and detects facial landmarks using MediaPipe's Face Mesh.
- The eye coordinates are mapped to the screen dimensions using PyAutoGUI.
- Blinking is detected by measuring the distance between specific eye landmarks.
- If the eye closing distance is below a certain threshold, a mouse click is triggered.

## Requirements

- Webcam
- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

Feel free to provide feedback or suggestions for improvement. You can reach me at Email: mfauzanfauzan123@gmail.com and: [Linkedin](https://www.linkedin.com/in/mfauzandsml/)
