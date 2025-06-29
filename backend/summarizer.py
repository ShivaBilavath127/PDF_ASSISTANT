from .together_client import chat_with_pdf

def generate_summary(text):
    prompt = f"Summarize the following document:\n\n{text}"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    return chat_with_pdf(messages)
