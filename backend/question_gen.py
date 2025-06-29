from .together_client import chat_with_pdf

def generate_questions(context, num_questions=3):
    prompt = f"Generate {num_questions} quiz-style questions from the following text:\n\n{context}"
    messages = [
        {"role": "system", "content": "You are a quiz master generating questions."},
        {"role": "user", "content": prompt}
    ]
    result = chat_with_pdf(messages)
    return result.strip().split("\n")[:num_questions]
