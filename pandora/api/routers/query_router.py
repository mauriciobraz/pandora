from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse

from ..models.query_models import QueryRequest, QueryResult

query_router = APIRouter(
    prefix="/query",
)


@query_router.post("", response_model=StreamingResponse, status_code=status.HTTP_200_OK)
async def submit_query(query_data: QueryRequest):
    raise HTTPException(status_code=501, detail="Not implemented yet")


@query_router.get("/{id}", response_model=QueryResult, status_code=status.HTTP_200_OK)
async def get_query_result(id: int):
    raise HTTPException(status_code=501, detail="Not implemented yet")
