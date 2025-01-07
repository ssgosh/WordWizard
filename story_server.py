import sys, os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS, cross_origin
import time

load_dotenv()

def load_prompt():
    with open("prompt.txt", "r") as f:
        return ''.join(f.readlines())


prompt = load_prompt()
print(prompt)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2048,
    "response_mime_type": "application/json",
}

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
