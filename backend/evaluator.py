from .together_client import chat_with_pdf

def evaluate_answer(question, user_answer, context):
    prompt = (
        f"Question: {question}\n\n"
        f"User's Answer: {user_answer}\n\n"
        f"Context: {context}\n\n"
        f"Evaluate the user's answer on a scale of 1 to 10. Just give the numeric score only."
    )
    messages = [
        {"role": "system", "content": "You are a strict evaluator scoring answers."},
        {"role": "user", "content": prompt}
    ]
    result = chat_with_pdf(messages)
    try:
        return float(result.strip())
    except:
        return 0.0
