from pydantic import BaseModel
from datetime import time


class contact_us(BaseModel):
    subject: str
    message: int
    user_id: int
