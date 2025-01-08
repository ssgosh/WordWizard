import sys, os
from flask import Flask, render_template
import google.generativeai as genai
from flask_cors import CORS, cross_origin
import time
import os
import time
import webview
import keyring


def load_prompt():
    with open("prompt.txt", "r") as f:
        return ''.join(f.readlines())


prompt = load_prompt()
print(prompt)

api_key = None


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

app = Flask(__name__, template_folder='./html')
CORS(app, supports_credentials=True)


@cross_origin()
@app.route('/api/story', methods=['GET'])
def get_story():
    if api_key is None:
        msg = "API Key is not set! Please set API key in the Settings Tab first"
        print(msg)
        return msg, 400

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
def default():
    if api_key is None:
        return render_template("settings.html")
    else:
        return render_template("word_wizard.html")


@app.route('/word_wizard.html')
def word_wizard():
    return render_template("word_wizard.html")


@app.route('/settings.html')
def settings():
    return render_template("settings.html")


## Below code is for webview
def get_api_key():
    global api_key
    api_key = keyring.get_password('WordWizard', 'GEMINI_API_KEY')
    if api_key is not None:
        configure_genai(api_key)
    return api_key


def set_api_key(key):
    global api_key
    api_key = key
    keyring.set_password('WordWizard', 'GEMINI_API_KEY', key)
    configure_genai(key)


def delete_api_key():
    global api_key
    api_key = None
    keyring.delete_password('WordWizard', 'GEMINI_API_KEY')
    configure_genai(None)


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
    # Retrieve api key 
    get_api_key()
    webview.create_window(
        'Word Wizard',
        app,
        js_api=api,
        text_select=True,
        confirm_close=True,
    )

    webview.start()

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
