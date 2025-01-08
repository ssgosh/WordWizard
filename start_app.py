import subprocess
import os
import time
import webview

# Start the Python server using waitress
server_script = os.path.join(os.path.dirname(__file__), 'story_server.py')
subprocess.Popen(['waitress-serve', '--listen=0.0.0.0:5000', 'story_server:app'])

# Wait for the server to start
time.sleep(5)

# Create a webview window to load the HTML page
webview.create_window('Word Wizard', 'word_wizard.html')
webview.start()
