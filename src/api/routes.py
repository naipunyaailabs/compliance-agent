# Directory: src/api/routes.py
from fastapi import APIRouter
from src.agent.workflow import workflow  # Import the workflow instance
from src.agent.nodes.vector_store import get_summaries

router = APIRouter()

@router.post("/scrape")
async def trigger_scraping():
    # Use the workflow instance's method
    result = await workflow.run_regulatory_workflow(url="")  # You'll need to provide the appropriate URL
    return {"message": "Scraping completed", "summary_count": len(result)}

@router.get("/summaries")
async def get_all_summaries(limit: int = 10):
    summaries = get_summaries(limit=limit)
    return {
        "summaries": summaries,
        "count": len(summaries)
    }
