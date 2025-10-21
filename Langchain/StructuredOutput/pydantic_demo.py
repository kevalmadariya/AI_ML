from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class Review(BaseModel):
    id: str = Field(..., description="Unique identifier of the review")
    summary: List[str] = Field(..., description="Write down summary in brief")
    sentiment: Literal["pos", "neg"] = Field(..., description="Return sentiment of the review discussed in the review in list")
    name: Optional[str] = Field(None, description="Write name of reviewer")
