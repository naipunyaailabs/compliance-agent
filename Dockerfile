FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Rename the file to match the import
RUN mv /app/src/agent/nodes/pdf_parser_.py /app/src/agent/nodes/pdf_parser.py

# Add this line to set PYTHONPATH
ENV PYTHONPATH=/app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

