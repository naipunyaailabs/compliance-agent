# Compliance Document Analysis System

A robust system for analyzing and summarizing compliance documents using AI-powered text analysis and vector storage.

## Features

- PDF document processing and analysis
- AI-powered document summarization using Groq API
- Vector storage using Weaviate for efficient document retrieval
- RESTful API endpoints for document processing and retrieval
- HTML report generation for document summaries
- Docker containerization for easy deployment

## Prerequisites

- Docker and Docker Compose
- Python 3.11 or higher
- Groq API key (for document summarization)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd compliance
```

2. Create a `.env` file in the root directory with the following variables:
```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=your_model_name
```

3. Build and start the containers:
```bash
docker-compose up --build
```

## Project Structure 
ompliance/
├── src/
│ ├── agent/
│ │ ├── nodes/
│ │ │ ├── vector_store.py # Vector storage operations
│ │ │ ├── summarizer.py # Document summarization
│ │ │ └── scraper.py # PDF scraping utilities
│ │ └── workflow.py # Main workflow orchestration
│ ├── api/
│ │ └── routes.py # API endpoints
│ └── config/
│ └── settings.py # Configuration settings
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## API Endpoints

### POST /scrape
Triggers the document scraping and processing workflow.

### GET /summaries
Retrieves stored document summaries.
- Query Parameters:
  - `limit` (optional): Number of summaries to retrieve (default: 10)

## Usage

1. Start the services:
```bash
docker-compose up
```

2. Access the API at `http://localhost:8000`

3. View generated summaries in the `reports` directory

## Development

### Local Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn src.main:app --reload
```

### Testing

Run the test suite:
```bash
python test_weaviate.py
```

## Dependencies

- FastAPI: Web framework
- Weaviate: Vector database
- Groq: AI summarization
- PDFPlumber: PDF processing
- BeautifulSoup4: Web scraping
- Docker: Containerization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Support

For support, please [add your support contact information]