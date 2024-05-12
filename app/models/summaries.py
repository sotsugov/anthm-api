from typing import List
from pydantic import BaseModel


class Summary(BaseModel):
    _id: str
    sessionId: str
    category: str
    content: str
    evaluation: List[dict]
