from ..Data.supabase import get_material_sb, get_materials_sb 
from fastapi import APIRouter
from ..models.material_model import material

router = APIRouter()


@router.get('/get_materials')
async def get_materials():
    try:
        response = get_materials_sb()
        return response
    except Exception as error:
        return {"error": error }
    
@router.get('/get_material/{material_id}')
async def get_material(material_id:int):
    try:
        response = get_material_sb(material_id)
        return response
    except Exception as error:
        return {"error": error }    

    