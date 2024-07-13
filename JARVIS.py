import openai
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('openai_key')
print(f"Loaded OpenAI API Key: {openai.api_key}")

if not openai.api_key:
    print("Error: OpenAI API key not found. Please check your .env file.")

@app.route('/')
def index():
    print("Serving the index.html page.")
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    print(f"Received user input: {user_input}")
    try:
        response = get_ai_response(user_input)
        print(f"AI response: {response}")
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in /ask route: {e}")
        return jsonify({'response': f"Error: {e}"})

def get_ai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use the correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        print(f"OpenAI API response: {response}")
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error in get_ai_response: {e}")
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
