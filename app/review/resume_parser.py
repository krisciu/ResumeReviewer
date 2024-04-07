# app/utils/resume_parser.py
import PyPDF2
import io

def parse_resume(file_bytes: bytes, content_type: str) -> str:
    if content_type == "application/pdf":
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return "\n".join(text)
    elif content_type == "text/plain":
        return file_bytes.decode('utf-8')
    else:
        raise ValueError("Unsupported file type")

