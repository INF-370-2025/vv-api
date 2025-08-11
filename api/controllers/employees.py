from ..Data.supabase import get_types_sb,get_type_sb,create_type_sb,update_type_sb,get_employees_sb,get_employee_sb, \
    create_employee_sb,update_employee_sb,get_pay_slips_sb,get_pay_slip_sb,create_pay_slip_sb,update_pay_slip_sb \
    ,get_employee_warnings_sb,get_employee_warning_sb,create_employee_warning_sb,update_employee_warning_sb,get_time_logs_sb,clock_in_sb,clock_out_sb, get_artisans_sb
from fastapi import APIRouter, HTTPException
from ..models.type_model import type
from ..models.employee_model import employee
from ..models.employee_pay_slip_model import employee_pay_slip
from ..models.employee_warning_model import employee_warning

router = APIRouter()

# Employee_type

@router.get('/get_types')
async def get_types():
    try:
        response = get_types_sb()
        return response
    except Exception as error:
        return {"error": error }  

@router.get('/get_type/{type_id}')
async def get_type(type_id:int):
    try:
        response = get_type_sb(type_id)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.post('/create_type')
async def create_type(type:type):
    try:
        response = create_type_sb(type)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.put('/update_type/{type_id}')
async def update_type(type_id:int,type:type):
    try:
        response = update_type_sb(type_id,type)
        return response
    except Exception as error:
        return {"error": error } 
    
# Employee

@router.get('/get_employees')
async def get_employees():
    try:
        response = get_employees_sb()
        return response
    except Exception as error:
        return {"error": error }  

@router.get('/get_employee/{employee_id}')
async def get_employee(employee_id:int):
    try:
        response = get_employee_sb(employee_id)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.post('/create_employee')
async def create_employee(employee:employee):
    try:
        response = create_employee_sb(employee)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.put('/update_employee/{employee_id}')
async def update_employee(employee_id:int,employee:employee):
    try:
        response = update_employee_sb(employee_id,employee)
        return response
    except Exception as error:
        return {"error": error } 
    
# Employee_pay_slip

@router.get('/get_pay_slips')
async def get_pay_slips():
    try:
        response = get_pay_slips_sb()
        return response
    except Exception as error:
        return {"error": error }  

@router.get('/get_pay_slip/{pay_slip_id}')
async def get_pay_slip(pay_slip_id:int):
    try:
        response = get_pay_slip_sb(pay_slip_id)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.post('/create_pay_slip')
async def create_pay_slip(pay_slip:employee_pay_slip):
    try:
        response = create_pay_slip_sb(pay_slip)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.put('/update_pay_slip/{pay_slip_id}')
async def update_pay_slip(pay_slip_id:int,pay_slip:employee_pay_slip):
    try:
        response = update_pay_slip_sb(pay_slip_id,pay_slip)
        return response
    except Exception as error:
        return {"error": error } 
    
#Employee_warning

@router.get('/get_employee_warnings')
async def get_employee_warnings():
    try:
        response = get_employee_warnings_sb()
        return response
    except Exception as error:
        return {"error": error }  

@router.get('/get_employee_warning/{employee_warning_id}')
async def get_employee_warning(employee_warning_id:int):
    try:
        response = get_employee_warning_sb(employee_warning_id)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.post('/create_employee_warning')
async def create_employee_warning(employee_warning:employee_warning):
    try:
        response = create_employee_warning_sb(employee_warning)
        return response
    except Exception as error:
        return {"error": error } 
    
@router.put('/update_employee_warning/{employee_warning_id}')
async def update_employee_warning(employee_warning_id:int,employee_warning:employee_warning):
    try:
        response = update_employee_warning_sb(employee_warning_id,employee_warning)
        return response
    except Exception as error:
        return {"error": error } 
    
    
@router.get('/get_time_logs')
async def get_time_logs():
    try:
        response = get_time_logs_sb()
        return response
    except Exception as error:
        return {"error": error }     
    
    
@router.post('/clock_in/{employee_id}')
async def clock_in(employee_id:int):
    try:
        response = clock_in_sb(employee_id)
        return response
    except Exception as error:
        return {"error": error }     
    
@router.post('/clock_out/{employee_id}')
async def clock_in(employee_id:int):
    try:
        response = clock_out_sb(employee_id)
        return response
    except Exception as error:
        return {"error": error }    
    
@router.get('/get_artisans')
async def get_artisans():
    result = get_artisans_sb()
    
    if isinstance(result, Exception):
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching artisans: {str(result)}"
        )
        
    return result