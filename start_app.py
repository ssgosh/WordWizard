import subprocess
import os
import time
import webview
import keyring
import tkinter as tk
from tkinter import simpledialog

def get_api_key():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    api_key = keyring.get_password('WordWizard', 'GEMINI_API_KEY')
    if api_key is None:
        api_key = simpledialog.askstring("API Key", "Enter your Gemini API Key:", show='*')
        if api_key:
            keyring.set_password('WordWizard', 'GEMINI_API_KEY', api_key)
    return api_key

# Ask the user for their Gemini API Key via GUI
api_key = get_api_key()

# Set the API Key as an environment variable
os.environ['GEMINI_API_KEY'] = api_key

# Start the Python server using waitress
server_script = os.path.join(os.path.dirname(__file__), 'story_server.py')
subprocess.Popen(['waitress-serve', '--listen=0.0.0.0:5000', 'story_server:app'])

time.sleep(1)

# Create a webview window to load the HTML page
webview.create_window('Word Wizard', 'word_wizard.html')
webview.start()
