import sys, os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS, cross_origin
import time
import os
import time
import webview
import keyring



# load_dotenv()

def load_prompt():
    with open("prompt.txt", "r") as f:
        return ''.join(f.readlines())


prompt = load_prompt()
print(prompt)

def configure_genai(api_key):
    genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2048,
    "response_mime_type": "application/json",
}

app = Flask(__name__, static_folder='./html', template_folder='./html')
CORS(app, supports_credentials=True)

@cross_origin()
@app.route('/api/story', methods=['GET'])
def get_story():
    t1 = time.time()
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )
    t2 = time.time()

    response = model.generate_content(prompt)
    t3 = time.time()

    print(response.text)
    print(f"Time taken for model creation: {t2 - t1}, for generation: {t3-t2}")
    return response.text

@app.route('/')
@app.route('/word_wizard.html')
def word_wizard():
    return render_template("word_wizard.html")


@app.route('/settings.html')
def word_wizard():
    return render_template("settings.html")

def get_api_key():
    return keyring.get_password('WordWizard', 'GEMINI_API_KEY')


def set_api_key(api_key):
    keyring.set_password('WordWizard', 'GEMINI_API_KEY', api_key)
    # os.environ['GEMINI_API_KEY'] = api_key
    configure_genai(api_key)


def delete_api_key():
    keyring.delete_password('WordWizard', 'GEMINI_API_KEY')
    # os.environ.pop('GEMINI_API_KEY', None)


class Api:

    def getApiKey(self):
        return get_api_key()

    def setApiKey(self, api_key):
        set_api_key(api_key)
        return "API Key saved successfully!"

    def deleteApiKey(self):
        delete_api_key()
        return "API Key deleted successfully!"


if __name__ == '__main__':
    api = Api()

    # Check if API key exists
    api_key = get_api_key()
    if api_key is None:
        webview.create_window('API Key Settings', 'settings.html', js_api=api)
    else:
        configure_genai(api_key)
        # os.environ['GEMINI_API_KEY'] = api_key
        # subprocess.Popen(['waitress-serve', '--listen=0.0.0.0:5000', 'story_server:app'])
        # time.sleep(0.1)
        webview.create_window('Word Wizard',
                            'word_wizard.html',
                            js_api=api,
                            text_select=True,
                            confirm_close=True,
                            )

    webview.start()



# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
