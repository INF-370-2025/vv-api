from pydantic import BaseModel
from datetime import time

class job_request(BaseModel):
    job_request_id:int
    customer_id:int
    design:str
    finish_date:str
    status:bool
    description:str
    job_request_status_id:int
    title:str
    quantity:int
    progress_url:str
    
    
    
class job_request_insert(BaseModel):
    customer_id:int
    finish_date:str
    description:str
    title:str
    quantity:int
