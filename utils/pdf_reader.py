from pdfminer.high_level import extract_text as extract_pdf_text
import tempfile

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name
            return extract_pdf_text(tmp_path)
        except Exception:
            return ""
    elif uploaded_file.type == "text/plain":
        try:
            return uploaded_file.read().decode("utf-8")
        except:
            return ""
    return ""
