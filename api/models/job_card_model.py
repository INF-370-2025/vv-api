# job_card_model.py
from pydantic import BaseModel
from typing import Optional

class job_card(BaseModel):
    job_card_id: int  
    pattern_id: Optional[int] = None
    job_card_status_id: Optional[int] = None
    quotation_id: Optional[int] = None
    special_instructions: Optional[str] = None
    completed_at: Optional[str] = None