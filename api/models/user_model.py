from pydantic import BaseModel


class user(BaseModel):
    name:str
    surname:str
    email_address:str
    phone_number:str
    role_id:int
    title_id:int
    image:str
    uuid:str
    is_employee:bool
