import subprocess
import os
import time
import webview
import keyring

def get_api_key():
    return keyring.get_password('WordWizard', 'GEMINI_API_KEY')

def set_api_key(api_key):
    keyring.set_password('WordWizard', 'GEMINI_API_KEY', api_key)
    os.environ['GEMINI_API_KEY'] = api_key

def delete_api_key():
    keyring.delete_password('WordWizard', 'GEMINI_API_KEY')
    os.environ.pop('GEMINI_API_KEY', None)

class Api:
    def getApiKey(self):
        return get_api_key()

    def setApiKey(self, api_key):
        set_api_key(api_key)
        return "API Key saved successfully!"

    def deleteApiKey(self):
        delete_api_key()
        return "API Key deleted successfully!"

api = Api()

# Check if API key exists
api_key = get_api_key()
if api_key is None:
    webview.create_window('API Key Settings', 'settings.html', js_api=api)
else:
    os.environ['GEMINI_API_KEY'] = api_key
    subprocess.Popen(['waitress-serve', '--listen=0.0.0.0:5000', 'story_server:app'])
    time.sleep(5)
    webview.create_window('Word Wizard', 'word_wizard.html', js_api=api, text_select=True)

webview.start()
