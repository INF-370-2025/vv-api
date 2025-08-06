from pydantic import BaseModel

class invoice(BaseModel):
    job_card_id:int
    total:float
    invoice_status_id:int
    invoice_url:str
    invoice_number:str