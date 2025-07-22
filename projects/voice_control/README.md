# Voice-Controlled Menu System

This is a Python-based voice-controlled menu system that can perform various tasks through voice commands.

## Features

- SSH login to remote machines
- Send WhatsApp messages
- Open applications (Notepad, Jupyter Notebook)
- Voice recognition and text-to-speech feedback

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your SSH password:
```
SSH_PASSWORD=your_password_here
```

3. Make sure you have a working microphone connected to your system.

## Usage

Run the program:
```bash
python voice_menu.py
```

### Available Voice Commands

- "SSH" or "login" - Start SSH login process
- "WhatsApp" or "message" - Send WhatsApp message
- "notepad" - Open Notepad
- "jupyter" or "notebook" - Open Jupyter Notebook
- "exit" or "quit" - Exit the program

## Notes

- For SSH login, you'll need to speak the IP address and username clearly
- For WhatsApp messages, speak the phone number with country code
- The program uses Google's speech recognition service, so an internet connection is required
- WhatsApp Web should be logged in for sending WhatsApp messages 