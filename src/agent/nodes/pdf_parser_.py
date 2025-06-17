import pdfplumber
import requests
from io import BytesIO

def extract_chunks_from_pdf(pdf_url):
    response = requests.get(pdf_url)
    with pdfplumber.open(BytesIO(response.content)) as pdf:
        chunks = []
        temp = ""
        for i, page in enumerate(pdf.pages):
            temp += page.extract_text() + "\n"
            if (i + 1) % 5 == 0:
                chunks.append(temp)
                temp = ""
        if temp:
            chunks.append(temp)
        return chunks