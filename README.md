# README.md

## Smart Assistant for Research Summarization

An AI-powered assistant that helps users interact with documents through:
- Automatic summarization
- Question answering
- Logic-based question generation and evaluation

### 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 📂 Features
- Upload PDF or TXT
- Get auto-summary (≤150 words)
- Ask anything based on content
- Get challenged with logic questions

### 📁 Folder Structure
```
project_folder/
├── app.py
├── requirements.txt
├── README.md
├── utils/
│   ├── pdf_handler.py
│   ├── summarizer.py
│   ├── qa_handler.py
│   ├── question_generator.py
│   └── evaluator.py
|   |__together_openai.py
├── static/
│   └── style.css (optional)
└── utils/
    └── pdf_reader.py
```

### 🔧 Optional
- Add style to `static/style.css`
- Deploy via Streamlit Cloud, Heroku, or AWS

### 🧠 Powered by
- Hugging Face Transformers
- Streamlit
- pdfminer.six
