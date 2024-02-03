from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(min_length=1, max_length=1024)


class QueryResult(BaseModel):
    result: str
    query_id: int
