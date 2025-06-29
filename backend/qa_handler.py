from .together_client import chat_with_pdf

def get_answer(context, question):
    messages = [
        {"role": "system", "content": "You are an expert assistant who answers based on the provided context."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
    ]
    return chat_with_pdf(messages)
