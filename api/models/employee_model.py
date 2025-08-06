from pydantic import BaseModel


class employee(BaseModel):
    job_scope:str
    address:str
    user_id:int
    emergency_contact:str
    hourly_rate:float