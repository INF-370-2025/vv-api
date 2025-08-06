from fastapi import APIRouter, Query
from ..Data.supabase import (get_employee_time_logs_sb, get_employee_time_log_sb, get_monthly_hours_worked)

router = APIRouter()

@router.get('/get_employee_time_logs')
async def get_employee_time_logs():
    try:
        response = get_employee_time_logs_sb()
        return response
    except Exception as error:
        return {"error": error }  

@router.get('/get_employee_time_log/{employee_time_log_id}')
async def get_employee_time_log(employee_time_log_id:int):
    try:
        response = get_employee_time_log_sb(employee_time_log_id)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.get('/monthly_hours_worked')
async def monthly_hours_worked_report(year: int = Query(..., description="Year to generate report for")):

    try:
        result = get_monthly_hours_worked(year)
        
        # Handle database errors
        if isinstance(result, dict) and 'error' in result:
            return {"error": result['error']}
            
        # Return sorted data by month number (should already be sorted but just in case)
        return sorted(result, key=lambda x: x['month_number'])
        
    except Exception as error:
        return {"error": error }