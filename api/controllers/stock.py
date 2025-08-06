from ..Data.supabase import get_stock_sb, create_stock_sb, update_stock_sb, get_all_stock_sb, get_stock_type_sb, get_stock_types_sb
from ..models.general_model import contact_us
from fastapi import APIRouter
from ..models.stock_model import stock

router = APIRouter()

#stock types

@router.get('/get_stock_types')
async def get_stock_types():
    try:
        response = get_stock_types_sb()
        return response
    except Exception as error:
        return {"error": error }  

@router.get('/get_stock_type/{stock_type_id}')
async def get_stock_type(stock_type_id:int):
    try:
        response = get_stock_type_sb(stock_type_id)
        return response
    except Exception as error:
        return {"error": error } 

#stock 

@router.get('/get_all_stock')
async def get_all_stock():
    try:
        response = get_all_stock_sb()
        return response
    except Exception as error:
        return {"error": error }
    
@router.get('/get_stock/{stock_id}')
async def get_stock(stock_id:int):
    try:
        response = get_stock_sb(stock_id)
        return response
    except Exception as error:
        return {"error": error }    

@router.post('/create_stock')
async def create_stock(stock:stock):
    try:
        response = create_stock_sb(stock)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.put('/update_stock/{stock_id}')
async def update_stock(stock_id:int,stock:stock):
    try:
        response = update_stock_sb(stock_id,stock)
        return response
    except Exception as error:
        return {"error": error }