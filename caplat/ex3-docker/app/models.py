from typing import Optional, List
from pydantic import BaseModel

class Response(BaseModel):
    result: Optional[int] = None
    errorMessage: Optional[str] = None

class CalculateRequest(BaseModel):
    arguments: List[int]
    operation: Optional[str] = ""

class Operation(BaseModel):
    flavor: str
    operation: str
    arguments: List[int]
    result: int

class HistoryResponse(BaseModel):
    result: Optional[List[Operation]] = None
    errorMessage: Optional[str] = None