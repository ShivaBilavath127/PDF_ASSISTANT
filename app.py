import streamlit as st
from utils.pdf_reader import extract_text_from_file
from backend.summarizer import generate_summary
from backend.qa_handler import get_answer
from backend.question_gen import generate_questions
from backend.evaluator import evaluate_answer

st.set_page_config(page_title="Smart PDF Assistant", layout="wide")
st.title("📄 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload PDF or TXT document", type=["pdf", "txt"])

if uploaded_file:
    document_text = extract_text_from_file(uploaded_file)
    if document_text.strip():
        summary = generate_summary(document_text)
        st.subheader("📝 Document Summary")
        st.write(summary)

        mode = st.radio("Choose Interaction Mode", ("Ask Anything", "Challenge Me"))

        if mode == "Ask Anything":
            question = st.text_input("❓ Ask Anything")
            if question:
                answer = get_answer(document_text, question)
                st.write(f"Answer: {answer}")

        elif mode == "Challenge Me":
            num_q = st.slider("Select number of questions", 1, 5, 3)
            if st.button("🧠 Start Challenge"):
                questions = generate_questions(document_text, num_q)
                for i, q in enumerate(questions):
                    user_ans = st.text_input(f"Q{i+1}: {q}", key=f"q_{i}")
                    if user_ans:
                        score = evaluate_answer(q, user_ans, document_text)
                        st.write(f"Score: {score:.2f}/10")
    else:
        st.error("❌ Could not extract valid text from this file. Please upload a proper PDF or TXT file.")
