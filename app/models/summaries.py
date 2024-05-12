from typing import List
from pydantic import BaseModel


class SummaryEvaluation(BaseModel):
    sentence: str
    isInferable: bool
    explanation: str


class Summary(BaseModel):
    _id: str
    sessionId: str
    category: str
    content: str
    evaluation: List[SummaryEvaluation]
