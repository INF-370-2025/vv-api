from typing import Optional
from ..Data.supabase import get_stock_sb, create_stock_sb, update_stock_sb, get_all_stock_sb, get_stock_type_sb, get_stock_types_sb, get_stock_export_sb
from ..models.general_model import contact_us
from fastapi import APIRouter
from ..models.stock_model import stock
from fastapi import Query
from ..services.excel_export import export_stock_to_excel
from fastapi.responses import StreamingResponse


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
    
#excel
@router.get('/export_stock_excel')
async def export_stock_excel():
    try:
        # Get only required fields
        stock_data = get_stock_export_sb()
        
        # Handle errors
        if isinstance(stock_data, Exception):
            return {"error": str(stock_data)}
        if not stock_data:
            return {"error": "No stock data found"}
        
        # Generate Excel file
        excel_file = export_stock_to_excel(stock_data)
        
        # Return as downloadable response
        return StreamingResponse(
            content=excel_file,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=stock_report.xlsx",
                "Access-Control-Expose-Headers": "Content-Disposition"
            }
        )
    except Exception as error:
        return {"error": str(error)}