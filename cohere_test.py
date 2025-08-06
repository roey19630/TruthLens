import cohere
import os
from dotenv import load_dotenv

# טען את קובץ הסביבה (.env)
load_dotenv()

# שלוף את המפתח מהסביבה
api_key = os.getenv("CO_API_KEY")

# התחברות לשירות
co = cohere.Client(api_key)

# שלח טקסט לבדיקה (נשתמש ביצירת טקסט - generate)
response = co.generate(
    model='command-light',
    prompt='Is the following sentence potentially misleading or biased? "Vaccines are a government conspiracy"',
    max_tokens=100
)

print("🔎 Cohere response:\n")
print(response.generations[0].text.strip())
