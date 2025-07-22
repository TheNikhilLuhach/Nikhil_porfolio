import cv2
import mediapipe as mp
import numpy as np
import subprocess
import time
import os
import pyautogui

class HandGestureController:
    def __init__(self):
        # Hand detection setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Track if processes are running
        self.notepad_process = None
        self.cmd_process = None
        self.jupyter_process = None
        
        # Cooldown timer for commands
        self.last_command_time = 0
        self.command_cooldown = 2  # seconds

    def detect_gesture(self, hand_landmarks):
        # Get finger states
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]

        # Get finger base positions
        index_base = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP]
        middle_base = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
        ring_base = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP]
        pinky_base = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP]

        # Check if fingers are extended
        index_extended = index_tip.y < index_base.y
        middle_extended = middle_tip.y < middle_base.y
        ring_extended = ring_tip.y < ring_base.y
        pinky_extended = pinky_tip.y < pinky_base.y

        # Count extended fingers
        extended_fingers = sum([index_extended, middle_extended, ring_extended, pinky_extended])

        # Detect punch (all fingers closed)
        is_punch = not (index_extended or middle_extended or ring_extended or pinky_extended)

        return {
            'extended_fingers': extended_fingers,
            'index_extended': index_extended,
            'middle_extended': middle_extended,
            'ring_extended': ring_extended,
            'pinky_extended': pinky_extended,
            'is_punch': is_punch
        }

    def minimize_all_windows(self):
        # Press Windows+D to minimize all windows
        pyautogui.hotkey('win', 'd')

    def execute_command(self, gesture):
        current_time = time.time()
        if current_time - self.last_command_time < self.command_cooldown:
            return

        # Punch detection - minimize all windows
        if gesture['is_punch']:
            self.minimize_all_windows()
            print("Minimized all windows")
            self.last_command_time = current_time
            return

        extended_fingers = gesture['extended_fingers']

        # One finger - Open Notepad
        if extended_fingers == 1:
            if self.notepad_process is None:
                self.notepad_process = subprocess.Popen(['notepad.exe'])
                print("Opened Notepad")
                self.last_command_time = current_time

        # Two fingers - Open CMD and run Python
        elif extended_fingers == 2:
            if self.cmd_process is None:
                self.cmd_process = subprocess.Popen(['cmd.exe', '/k', 'python'])
                print("Opened CMD with Python")
                self.last_command_time = current_time

        # Three fingers - Open new CMD and run Jupyter Notebook
        elif extended_fingers == 3:
            if self.jupyter_process is None:
                self.jupyter_process = subprocess.Popen(['cmd.exe', '/k', 'jupyter notebook'])
                print("Launched Jupyter Notebook")
                self.last_command_time = current_time

    def run(self):
        cap = cv2.VideoCapture(0)
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Failed to read from webcam")
                continue

            # Flip the image horizontally for a later selfie-view display
            image = cv2.flip(image, 1)
            
            # Convert the BGR image to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Process hand detection
            hand_results = self.hands.process(image_rgb)

            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    # Draw hand landmarks
                    self.mp_draw.draw_landmarks(
                        image, 
                        hand_landmarks, 
                        self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Detect gesture and execute command
                    gesture = self.detect_gesture(hand_landmarks)
                    self.execute_command(gesture)

            # Display the image
            cv2.imshow('Hand Gesture Control', image)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Clean up
        cap.release()
        cv2.destroyAllWindows()
        
        # Close any running processes
        if self.notepad_process:
            self.notepad_process.terminate()
        if self.cmd_process:
            self.cmd_process.terminate()
        if self.jupyter_process:
            self.jupyter_process.terminate()

if __name__ == "__main__":
    controller = HandGestureController()
    controller.run() 