from pydantic import BaseModel

class delivery_note(BaseModel):
    delivery_note_id: int
    job_card_id: int
    delivery_note_url: str