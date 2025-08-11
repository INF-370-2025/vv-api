from http.client import HTTPException
from fastapi import APIRouter
from ..Data.supabase import (
    get_job_cards_sb,
    get_job_card_sb,
    create_job_card_sb,
    update_job_card_sb,
    get_job_card_statuses_sb,
    get_job_card_status_sb, 
    get_completed_job_cards_sb,
    get_job_card_with_materials_sb,
    get_job_card_artisans_sb,
    get_job_card_update_sb
)
from ..models.job_card_model import job_card, JobCardWithMaterials, JobCardUpdate, JobCardCreate

router = APIRouter()

@router.get('/get_job_card_statuses')
async def get_job_card_statuses():
    return get_job_card_statuses_sb()

@router.get('/get_job_card_status/{job_card_status_id}')
async def get_job_card_status(job_card_status_id: int):
    return get_job_card_status_sb(job_card_status_id)

# Job Card Endpoints
@router.get('/get_job_cards')
async def get_job_cards():
    return get_job_cards_sb()

@router.get('/get_job_card/{job_card_id}')
async def get_job_card(job_card_id: int):
    return get_job_card_sb(job_card_id)

@router.get('/get_job_card_update/{job_card_id}')
async def get_job_card_update(job_card_id: int):
    return get_job_card_update_sb(job_card_id)

@router.post('/create_job_card')
async def create_job_card(job_card: JobCardCreate):  
    return create_job_card_sb(job_card)

@router.put('/update_job_card/{job_card_id}')
async def update_job_card(job_card_id: int, update_data: JobCardUpdate):
    return update_job_card_sb(job_card_id, update_data.dict())

@router.get('/get_completed_job_cards')
async def get_completed_job_cards():
    return get_completed_job_cards_sb()

@router.get('/get_job_card_with_materials/{job_card_id}', response_model=JobCardWithMaterials)
async def get_job_card_with_materials(job_card_id: int):
    result = get_job_card_with_materials_sb(job_card_id)
    
    if isinstance(result, Exception):
        raise HTTPException(
            status_code=500, 
            detail=f"Error fetching job card: {str(result)}"
        )
    if not result:
        raise HTTPException(
            status_code=404, 
            detail="Job card not found"
        )
    
    return result

@router.get('/get_job_card_artisans/{job_card_id}')
async def get_job_card_artisans(job_card_id: int):
    return get_job_card_artisans_sb(job_card_id)