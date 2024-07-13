
# JARVIS: AI Unraveled

JARVIS is an AI-powered web application designed to provide cutting-edge AI technology through an interactive voice interface. This project demonstrates the integration of Flask with the Web Speech API for both speech recognition and speech synthesis.

## Features

- **Smart Analysis**: Leverage our AI for in-depth data analysis and insights.
- **Automated Tasks**: Automate routine tasks and boost your productivity.
- **Real-Time Reporting**: Get real-time updates and reports on your data.
- **Voice Interaction**: Interact with the AI using voice commands.

## Requirements

- Python 3.6+
- Flask
- OpenAI API Key
- Web Browser with Web Speech API support

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/jarvis-ai.git
   cd jarvis-ai
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install flask openai python-dotenv
   ```

4. **Set up the `.env` file**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   openai_key=your_openai_api_key_here
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python JARVIS.py
   ```

2. **Access the web application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
jarvis-ai/
│
├── static/
│   ├── main.css
│   └── func.js
│
├── templates/
│   └── index.html
│
├── .env
├── JARVIS.py
└── README.md
```

## JARVIS.py

This is the main Flask application file. It sets up the web server and handles communication with the OpenAI API.

## index.html

This file contains the HTML structure and integrates with the Web Speech API for speech recognition and synthesis.

## main.css

This file contains the CSS styles for the web application.

## func.js

This file contains additional JavaScript functions for the web application.

## Customization

- **Changing the Voice**: You can change the voice used for speech synthesis by modifying the `speak` function in `index.html` to select a different voice.
- **Adding Features**: You can add more features to the AI by updating the backend Flask routes and the frontend HTML/JavaScript.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
