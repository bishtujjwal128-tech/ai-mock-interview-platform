import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_questions(skills):

    prompt = f"""
    Generate 10 technical interview questions
    based on these skills:

    {skills}
    """

    response = model.generate_content(prompt)

    return response.text