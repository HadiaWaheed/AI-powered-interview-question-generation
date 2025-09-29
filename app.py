import os
import json
from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Flask app
app = Flask(__name__)

# Groq client
client = Groq(api_key=groq_api_key)

# Preferred models (fallback order)
SUPPORTED_MODELS = [
    "llama-3.1-8b-instant",     # ✅ fast & cheap
    "llama-3.1-70b-versatile"   # ✅ higher quality fallback
]

# -------------------------
# Home Page
# -------------------------
@app.route('/')
def index():
    return render_template('index.html')

# -------------------------
# About Page
# -------------------------
@app.route('/about')
def about():
    return render_template('about.html')

# -------------------------
# Generate Questions
# -------------------------
@app.route('/generate', methods=['POST'])
def generate():
    role = request.form['role']

    prompt = f"""
    Generate 5 technical and 5 behavioral interview questions 
    for the role of {role}. 

    ⚠️ Important:
    - Return valid JSON format only
    - Two keys: "technical" and "behavioral"
    - Each contains a list of questions as plain strings
    - Do NOT add points, explanations, or extra text
    Example format:
    {{
        "technical": ["Q1", "Q2", "Q3", "Q4", "Q5"],
        "behavioral": ["Q1", "Q2", "Q3", "Q4", "Q5"]
    }}
    """

    for model in SUPPORTED_MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            # Extract response
            raw_text = response.choices[0].message.content.strip()

            # Ensure JSON
            cleaned_json = json.loads(raw_text)

            return render_template(
                'result.html',
                role=role,
                questions=cleaned_json
            )

        except Exception as e:
            print(f"⚠️ Model {model} failed: {str(e)}")
            continue  # try the next model

    # If all models fail
    return "⚠️ Error: All available models failed. Please try again later."

# -------------------------
# Run App
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
