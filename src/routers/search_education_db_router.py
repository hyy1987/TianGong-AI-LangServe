from fastapi import APIRouter, HTTPException

from src.models.models import SearchResponse, VectorSearchRequestWithCourse
from src.services.standalone import search_education_db

router = APIRouter()


@router.post(
    "/search_education_db",
    response_model=SearchResponse,
    response_description="List of documents matching the query",
)
async def search_vectors(request: VectorSearchRequestWithCourse):
    """
    This endpoint allows you to perform a semantic search in an educational documents vector database.
    It takes a query string as input and returns a list of documents that match the query.

    - **query**: The search query string
    - **top_k**: The number of documents to return (default 16)
    - **course**: The course to search in (default None)
    """
    try:
        result = await search_education_db.search(request.query, request.top_k, request.course)
        return SearchResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
