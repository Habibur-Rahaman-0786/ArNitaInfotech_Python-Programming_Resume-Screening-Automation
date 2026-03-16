from pdfminer.high_level import extract_text
import docx

def extract_text_from_pdf(file_path):
    text = extract_text(file_path)
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

def get_resume_text(file_path):

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        return "Unsupported file format"