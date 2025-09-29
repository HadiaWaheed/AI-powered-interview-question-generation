# 🤖 AI-Powered Interview Question Generator

## 🚀 Project Overview

This web app allows users to enter a **role or skill**, and it generates:

* ✅ 5 **Technical Questions**
* ✅ 5 **Behavioral Questions**

**Features:**

* Clean interface with modern styling
* AI-powered question generation via **Groq API**
* Flask-based backend
* Dynamic display of questions in a user-friendly format

---

## 📁 Project Structure

```
ai-interview-generator/
│
├─ templates/
│  ├─ base.html
│  ├─ index.html
│  └─ result.html
│
├─ static/
│  └─ style.css
│
├─ .env                # API key and secret
├─ requirements.txt
├─ app.py              # Main Flask application
└─ README.md
```

---

## ⚡ Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/ai-interview-generator.git
cd ai-interview-generator
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add `.env` file with:

```
GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=your_flask_secret_here
```

---

## 🏃 Run the App

```bash
python app.py
```

Open your browser at: `http://127.0.0.1:5000/`

Enter a role/skill → Click **Generate Questions** → See technical & behavioral questions instantly!

---
## 🔧 Tech Stack

* **Python 3.11**
* **Flask 2.3**
* **Groq API** (AI text generation)
* **HTML / CSS** for frontend

---

## ✨ Future Enhancements

* Add **role categories** for predefined question sets
* Store generated questions in a database for **analytics**
* Add **downloadable PDF** feature for interview prep

---

## 📜 License

MIT License © [Hadia Waheed]
