# app.py

from flask import Flask, render_template, request
import cohere
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
api_key = os.getenv("CO_API_KEY")

# Initialize Cohere client
co = cohere.Client(api_key)

app = Flask(__name__)

def analyze_text(text: str) -> str:
    prompt = f"""Analyze the following statement for potential misinformation, bias, or lack of evidence.
Be objective and clear. Provide a short explanation.

Statement:
{text}

Response:"""

    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    return response.generations[0].text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        result = analyze_text(user_input)

        # Save to log file
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"--- {datetime.now()} ---\n")
            f.write(f"Input: {user_input}\n")
            f.write(f"Response: {result}\n\n")

    return render_template("index.html", result=result, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
