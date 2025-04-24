import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file to access API keys
load_dotenv()

# Initialize Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a model instance
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_email(subject: str, recipient: str, message: str, sender: str, tone: str) -> str:
    prompt = f"""
Write an email in a {tone.lower()} tone with the following details:

Subject: {subject}
Recipient: {recipient}
Message: {message}
Sender: {sender}

Include sender details (name and email) properly at the end.
Return the email body text only.
"""
    response = model.generate_content(prompt)
    email_content = response.text.strip()
    return email_content

