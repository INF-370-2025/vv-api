from ..Data.supabase import get_titles_sb,contact_us_sb,get_admin_stats_sb,get_artisan_stats_sb
from ..models.general_model import contact_us
from fastapi import APIRouter

router = APIRouter()

@router.get('/get_titles')
async def get_titles():
    try:
        response = get_titles_sb()
        return response
    except Exception as error:
        return {"error": error }
       
@router.post('/contact_us')
async def contact_us(contact:contact_us):
    try:
        response = contact_us_sb(contact)
        return response
    except Exception as error:
        return {"error": error }
    
@router.get('/get_admin_stats')
async def get_admin_stats():
    try:
        response = get_admin_stats_sb()
        return response
    except Exception as error:
        return {"error": error }   
    
@router.get('/get_artisan_stats/{user_id}')
async def get_artisan_stats(user_id: int):
    try:
        response = get_artisan_stats_sb(user_id)
        return response
    except Exception as error:
        return {"error": error }   
        
    
    
    
    
    
    
    