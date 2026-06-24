skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "numpy",
    "pandas",
    "nlp",
    "gen ai",
    "langchain"
]

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found