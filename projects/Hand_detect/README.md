# Hand Gesture Control Program

This program uses your computer's webcam to detect hand gestures and perform various commands. It can open applications and minimize all windows using simple hand gestures.

## Requirements

- Python 3.7 or higher
- Webcam
- Required Python packages (install using `pip install -r requirements.txt`):
  - opencv-python
  - mediapipe
  - numpy
  - pyautogui

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```
   python hand_gesture_control.py
   ```

2. Gesture Commands:
   - Show one finger: Opens Notepad
   - Show two fingers: Opens CMD and runs Python
   - Show three fingers: Opens new CMD and launches Jupyter Notebook
   - Make a fist (punch): Minimizes all windows (Windows+D)

3. Additional Features:
   - Hand Landmarks: Displays hand landmarks for better gesture recognition

4. To quit the program, press 'q' on your keyboard

## Notes

- Make sure you have good lighting for better detection
- Keep your hand within the camera frame
- There's a 2-second cooldown between commands to prevent accidental triggers
- The program will automatically close any opened applications when you quit 