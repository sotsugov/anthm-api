from pydantic import BaseModel
from typing import List


class Session(BaseModel):
    _id: str
    customerId: str
    assessorId: str
    startTime: str
    endTime: str
    selectedCategories: List[str]
    status: str
