from ..Data.supabase import get_invoices_sb, get_invoices_user_sb, log_error, update_invoice_status_sb, update_invoice_sb, get_unpaid_invoices, create_invoice_sb, update_invoice_pop_sb
from fastapi import APIRouter
from ..models.quotation_model import quotation
from ..models.invoice_model import invoice

router = APIRouter()


#invoices    
@router.get('/get_invoices')
async def get_invoices():
    try:
        response = get_invoices_sb()
        return response
    except Exception as error:
        return {"error": error }  
    
@router.get('/get_invoices_user/{user_id}')
async def get_invoices_user(user_id:int):
    try:
        response = get_invoices_user_sb(user_id)
        return response
    except Exception as error:
        return {"error": error } 


@router.put('/update_invoice/{invoice_id}')
async def update_invoice(invoice_id:int,invoice:invoice):
     try:
         response = update_invoice_sb(invoice_id,invoice)
         return response
     except Exception as error:
         return {"error": error } 
    
@router.put('/update_invoice_status/{invoice_id}')
async def update_invoice_status(invoice_id: int):
    return update_invoice_status_sb(invoice_id)

@router.get('/unpaid_invoices')
async def unpaid_invoices_report():
    try:
        result = get_unpaid_invoices()
        
        # Handle database errors
        if isinstance(result, dict) and 'error' in result:
            return {"error": result['error']}
            
        # Return sorted data by invoice number
        return sorted(result, key=lambda x: x['invoice_number'])
        
    except Exception as error:
        return {"error": str(error)}
    
    
@router.post('/create_invoice')
async def create_invoice(invoice:invoice):
    try:
        response = create_invoice_sb(invoice)
        return response
    except Exception as error:
        return {"error": error } 
    
    
@router.patch('/update_invoice_pop/{invoice_id}')
async def update_invoice_pop(invoice_id: int, data: dict):
    """
    Update Proof of Payment for an invoice
    """
    try:
        if 'pop' not in data or not data['pop']:
            return {"error": "POP URL is required"}
            
        response = update_invoice_pop_sb(invoice_id, data['pop'])
        return response
    except Exception as error:
        log_error(f"Error updating POP: {error}")
        return {"error": str(error)}