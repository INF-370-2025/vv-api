from fastapi import APIRouter
from ..Data.supabase import (
    get_job_cards_sb,
    get_job_card_sb,
    create_job_card_sb,
    update_job_card_sb,
    get_job_card_statuses_sb,
    get_job_card_status_sb, 
    get_completed_job_cards_sb
)
from ..models.job_card_model import job_card

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

@router.post('/create_job_card')
async def create_job_card(job_card: job_card):
    return create_job_card_sb(job_card)

@router.put('/update_job_card/{job_card_id}')
async def update_job_card(job_card_id: int, job_card: job_card):
    return update_job_card_sb(job_card_id, job_card)

@router.get('/get_completed_job_cards')
async def get_completed_job_cards():
    return get_completed_job_cards_sb()