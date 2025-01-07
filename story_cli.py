import sys, os
import google.generativeai as genai

def load_prompt():
    with open("prompt.txt", "r") as f:
        return ''.join(f.readlines())
prompt = load_prompt()
# print(prompt)
# sys.exit(1)
GEMINI_API_KEY=os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 2048,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

response = model.generate_content(prompt)

print(response)
print(response.text)
print(type(response.text))
