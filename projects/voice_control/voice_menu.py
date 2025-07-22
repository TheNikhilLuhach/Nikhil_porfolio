import speech_recognition as sr
import pyttsx3
import pywhatkit
import paramiko
import os
import subprocess
import time
import webbrowser
import pyautogui
import win32gui
import win32con
from colorama import init, Fore, Style
import msvcrt
import logging
from functools import wraps
from dotenv import load_dotenv

init()
load_dotenv()
logging.basicConfig(filename='voice_menu.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_time(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        try:
            result = func(self, *args, **kwargs)
            logging.info(f"{func.__name__} | Args: {args} | Time: {time.time()-start:.2f}s")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} | Error: {e}")
            print(f"Error: {e}")
    return wrapper

class VoiceMenu:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.assistant_name = "Alexa"
        self.command_keys = [
            "send_whatsapp", "ssh_login", "open_notepad", "open_jupyter", "google_search",
            "minimize_all", "minimize", "maximize", "close_window", "help", "exit", "log"
        ]
        # Assign numbers to commands in the dictionary
        self.commands = {}
        for idx, key in enumerate(self.command_keys, 1):
            if key == "send_whatsapp":
                variations = ["send whatsapp", "send message", "whatsapp message", "send a message", "whatsapp", "send msg", "message bhejo", "message send", "whatsapp bhejo"]
            elif key == "ssh_login":
                variations = ["ssh login", "login ssh", "connect ssh", "remote login", "ssh connect", "remote connect", "connect system", "ssh"]
            elif key == "open_notepad":
                variations = ["open notepad", "start notepad", "launch notepad", "notepad open", "note pad", "notes", "open notes", "start notes", "notepad"]
            elif key == "open_jupyter":
                variations = ["open jupyter", "start jupyter", "launch jupyter", "jupyter notebook", "jupyter", "notebook", "python notebook", "start notebook"]
            elif key == "google_search":
                variations = ["google search", "search google", "search for", "google it", "search", "find", "look for", "google", "search karo"]
            elif key == "minimize_all":
                variations = ["minimize all", "minimize windows", "hide all windows", "hide windows", "minimize sab", "sab minimize", "hide all"]
            elif key == "minimize":
                variations = ["minimize", "minimize window", "window minimize", "chota karo", "minimize karo"]
            elif key == "maximize":
                variations = ["maximize", "maximize window", "window maximize", "bada karo", "maximize karo"]
            elif key == "close_window":
                variations = ["close window", "close current window", "band karo", "window band", "close", "band", "window close", "close karo"]
            elif key == "help":
                variations = ["help", "show help", "what can you do", "commands", "help me", "show commands", "guide", "help karo", "commands dikhao"]
            elif key == "exit":
                variations = ["exit", "quit", "close", "band karo", "bye bye", "goodbye", "quit karo", "band kar do", "exit karo", "bye"]
            elif key == "log":
                variations = ["log", "show log", "logs", "view log", "log file"]
            self.commands[key] = [str(idx)] + variations

    def speak(self, text):
        print(f"{self.assistant_name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except:
                return None

    def get_command(self):
        print("Press 'T' to type or speak your command...")
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 't':
                    return input("Type your command: ").lower()
            command = self.listen()
            if command:
                return command

    def show_help(self):
        print("Available Commands:")
        for idx, key in enumerate(self.command_keys, 1):
            print(f"{idx}. {key.replace('_', ' ')}: {self.commands[key][1]}")

    def match_command(self, command):
        command = command.strip()
        # Match by number string or by text
        for key, variations in self.commands.items():
            if command in variations:
                return key
        return None

    @log_and_time
    def ssh_login(self):
        ip = input("Enter SSH IP: ")
        user = input("Enter SSH username: ")
        password = os.getenv('SSH_PASSWORD')
        if not password:
            print("SSH password not found in .env")
            return
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=user, password=password, timeout=10)
            print(f"Connected to {ip}")
            while True:
                cmd = input("Enter Linux command (or 'exit ssh'): ")
                if 'exit ssh' in cmd:
                    break
                stdin, stdout, stderr = ssh.exec_command(cmd)
                print(stdout.read().decode())
            ssh.close()
        except Exception as e:
            print(f"SSH error: {e}")

    @log_and_time
    def send_whatsapp(self):
        phone = input("Enter phone number with country code: ")
        msg = input("Enter message: ")
        try:
            pywhatkit.sendwhatmsg_instantly(phone, msg)
            time.sleep(2)
            pyautogui.press('enter')
            print("Message sent!")
        except Exception as e:
            print(f"WhatsApp error: {e}")

    @log_and_time
    def open_application(self, app):
        try:
            if app == "notepad":
                subprocess.Popen("notepad.exe")
            elif app == "jupyter":
                subprocess.Popen(["jupyter", "notebook"])
            else:
                print(f"Unknown app: {app}")
        except Exception as e:
            print(f"App error: {e}")

    @log_and_time
    def google_search(self):
        query = input("What to search for? ")
        try:
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        except Exception as e:
            print(f"Search error: {e}")

    @log_and_time
    def window_management(self, action):
        try:
            if action == "minimize all":
                pyautogui.hotkey('winleft', 'd')
            elif action == "minimize":
                hwnd = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            elif action == "maximize":
                hwnd = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            elif action == "close":
                pyautogui.hotkey('alt', 'f4')
        except Exception as e:
            print(f"Window error: {e}")

    @log_and_time
    def show_log(self):
        pwd = input("Enter log password: ")
        if pwd == "password":
            try:
                with open("voice_menu.log") as f:
                    print(f.read())
            except Exception as e:
                print(f"Log error: {e}")
        else:
            print("Incorrect password.")

    def transcribe_audio_file(self, audio_path):
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
            return self.recognizer.recognize_google(audio).lower()
        except Exception as e:
            return None

    def run(self):
        self.speak(f"Hello! I'm {self.assistant_name}. Say '{self.assistant_name}' to wake me up!")
        self.show_help()
        while True:
            command = self.get_command()
            cmd_key = self.match_command(command)
            if not cmd_key:
                self.speak("Unknown command. Say 'help' to see available commands.")
                continue
            if cmd_key == "help":
                self.show_help()
            elif cmd_key == "exit":
                self.speak("Goodbye!")
                break
            elif cmd_key == "ssh_login":
                self.ssh_login()
            elif cmd_key == "send_whatsapp":
                self.send_whatsapp()
            elif cmd_key == "open_notepad":
                self.open_application("notepad")
            elif cmd_key == "open_jupyter":
                self.open_application("jupyter")
            elif cmd_key == "google_search":
                self.google_search()
            elif cmd_key == "minimize_all":
                self.window_management("minimize all")
            elif cmd_key == "minimize":
                self.window_management("minimize")
            elif cmd_key == "maximize":
                self.window_management("maximize")
            elif cmd_key == "close_window":
                self.window_management("close")
            elif cmd_key == "log":
                self.show_log()

    def run_command(self, command, log_password=None):
        cmd_key = self.match_command(command)
        if not cmd_key:
            return "Unknown command. Say 'help' to see available commands."
        if cmd_key == "help":
            return '\n'.join([f"{i+1}. {k.replace('_',' ')}: {self.commands[k][1]}" for i, k in enumerate(self.command_keys)])
        elif cmd_key == "exit":
            return "Goodbye!"
        elif cmd_key == "ssh_login":
            return "SSH login only available in terminal mode."
        elif cmd_key == "send_whatsapp":
            return "WhatsApp only available in terminal mode."
        elif cmd_key == "open_notepad":
            return "Notepad can only be opened in terminal mode."
        elif cmd_key == "open_jupyter":
            return "Jupyter can only be opened in terminal mode."
        elif cmd_key == "google_search":
            return "Google search only available in terminal mode."
        elif cmd_key == "minimize_all":
            return "Window management only available in terminal mode."
        elif cmd_key == "minimize":
            return "Window management only available in terminal mode."
        elif cmd_key == "maximize":
            return "Window management only available in terminal mode."
        elif cmd_key == "close_window":
            return "Window management only available in terminal mode."
        elif cmd_key == "log":
            if log_password == "password":
                try:
                    with open("voice_menu.log") as f:
                        return f.read()
                except Exception as e:
                    return f"Log error: {e}"
            else:
                return "Incorrect password."
        return "Command not supported in web mode."

if __name__ == "__main__":
    VoiceMenu().run() 