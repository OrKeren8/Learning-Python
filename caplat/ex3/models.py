from typing import Optional
from pydantic import BaseModel

class Response(BaseModel):
    result: Optional[int] = None
    errorMessage: Optional[str] = None