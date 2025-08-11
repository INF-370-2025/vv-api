# job_card_model.py
from pydantic import BaseModel
from typing import Optional, List

class job_card(BaseModel):
    job_card_id: int  
    pattern_id: Optional[int] = None
    job_card_status_id: Optional[int] = None
    quotation_id: Optional[int] = None
    special_instructions: Optional[str] = None
    completed_at: Optional[str] = None
    
class Material(BaseModel):
    material_id: int
    material_name: str

class JobCardBase(BaseModel):
    job_card_id: int
    created_at: Optional[str] = None
    special_instructions: Optional[str] = None
    job_card_status_id: Optional[int] = None
    pattern_id: Optional[int] = None
    quotation_id: Optional[int] = None
    completed_at: Optional[str] = None

class JobCardWithMaterials(JobCardBase):
    materials: List[Material] = []
    
class JobCardUpdate(BaseModel):
    pattern_id: Optional[int] = None
    job_card_status_id: Optional[int] = None
    quotation_id: Optional[int] = None
    special_instructions: Optional[str] = None
    completed_at: Optional[str] = None
    materials: Optional[List[int]] = None
    artisans: Optional[List[int]] = None