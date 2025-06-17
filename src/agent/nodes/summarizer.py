import httpx
import json
from typing import List
from src.config.settings import settings
from src.utils.logging import logger

class SummarizationError(Exception):
    """Custom exception for summarization errors"""
    pass

def summarize_chunks(chunks: List[str]) -> List[str]:
    """
    Summarize text chunks using the Groq API.
    
    Args:
        chunks (List[str]): List of text chunks to summarize
        
    Returns:
        List[str]: List of summaries
        
    Raises:
        SummarizationError: If there's an error during summarization
    """
    if not chunks:
        return []
        
    summaries = []
    headers = {
        "Authorization": f"Bearer {settings.groq_api_key}",
        "Content-Type": "application/json"
    }
    
    for i, chunk in enumerate(chunks, 1):
        try:
            # More specific system prompt
            system_prompt = """You are a compliance analyst. Your task is to:
            1. Analyze the provided document thoroughly
            2. Extract key compliance requirements and obligations
            3. Identify specific regulatory references and standards
            4. Note any deadlines or time-sensitive requirements
            5. Highlight any potential compliance risks or concerns
            
            Provide a detailed, document-specific summary that captures these elements."""
            
            payload = {
                "model": settings.model_name,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Please analyze and summarize this compliance document:\n\n{chunk[:3000]}"}
                ],
                "temperature": 0.7  # Increased temperature for more varied outputs
            }
            
            response = httpx.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            
            result = response.json()
            summary = result["choices"][0]["message"]["content"]
            
            # Add chunk identifier to help track which part of the document is being summarized
            summary = f"[Chunk {i}/{len(chunks)}]\n{summary}"
            summaries.append(summary)
            
            logger.info(f"Successfully summarized chunk {i}/{len(chunks)}")
            
        except httpx.HTTPError as e:
            error_msg = f"HTTP error occurred while summarizing chunk {i}: {str(e)}"
            logger.error(error_msg)
            raise SummarizationError(error_msg)
            
        except json.JSONDecodeError as e:
            error_msg = f"Failed to parse API response for chunk {i}: {str(e)}"
            logger.error(error_msg)
            raise SummarizationError(error_msg)
            
        except Exception as e:
            error_msg = f"Unexpected error while summarizing chunk {i}: {str(e)}"
            logger.error(error_msg)
            raise SummarizationError(error_msg)
            
    return summaries
