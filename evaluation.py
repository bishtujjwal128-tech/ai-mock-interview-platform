import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def evaluate(question, answer):

    prompt = f"""
    Question:
    {question}

    Candidate Answer:
    {answer}

    Give:

    Technical Score out of 10
    Communication Score out of 10
    Improvement Suggestions
    """

    response = model.generate_content(
        prompt
    )

    return response.text