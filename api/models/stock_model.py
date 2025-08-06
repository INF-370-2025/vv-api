from pydantic import BaseModel

class stock(BaseModel):
    stock_id: int
    stock_type_id: int
    material_id: int
    name: str
    description: str
    stock_level: int
    price: int