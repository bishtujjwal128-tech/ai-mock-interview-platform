import streamlit as st
from parser import extract_text
from skills import extract_skills
from questions import generate_questions
from evaluation import evaluate

st.set_page_config(
    page_title="AI Mock Interview Platform",
    layout="wide"
)

st.title("🎤 AI Mock Interview Platform")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if resume:

    text = extract_text(resume)

    skills = extract_skills(text)

    st.write("Skills Found")

    st.write(skills)

    if st.button(
        "Generate Questions"
    ):

        questions = generate_questions(
            skills
        )

        st.write(questions)

question = st.text_input(
    "Question"
)

answer = st.text_area(
    "Your Answer"
)

if st.button(
    "Evaluate Answer"
):

    result = evaluate(
        question,
        answer
    )

    st.write(result)