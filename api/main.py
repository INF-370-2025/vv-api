from fastapi import FastAPI, Request
import os 

from fastapi.responses import RedirectResponse
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from .controllers import roles, users, employees, receipt, job_cards,quotations, roles ,  customer, job_request, general , stock, invoices, pattern, material, delivery_notes, employee_time_logs
from dotenv import load_dotenv
from .Data.supabase import set_users

app = FastAPI(title="Vault Vision API", version="1.0.0", swagger_ui_parameters={"displayRequestDuration":True, "persistAuthorization":True})

load_dotenv(verbose=True)

############### ENV #####################

print("ENVIRONMENT", os.getenv("FASTAPI_ENV"))
print("CREDENTIALS", settings)

############### ENV #####################



############### ORIGINS #####################

origins_dev = ['*']
origins_prod = ['https://www.foundryzne.co.za','https://foundryzone.co.za',]

FASTAPI_ENV = os.getenv("FASTAPI_ENV")
origins = origins_dev if FASTAPI_ENV == "dev" else origins_prod
app.add_middleware(CORSMiddleware,
                   allow_origins=origins, 
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'],     
                   )

############### ORIGINS #####################




############### ENDPOINTS #####################

app.include_router(roles.router,prefix='/roles',tags=['Roles'])
app.include_router(quotations.router,prefix='/quotations',tags=['Quotations'])
app.include_router(invoices.router,prefix='/invoices',tags=['Invoices'])
app.include_router(job_cards.router,prefix='/job_cards',tags=['Job Cards'])
app.include_router(users.router,prefix='/users',tags=['Users'])
app.include_router(employees.router,prefix='/employees',tags=['Employees'])
app.include_router(receipt.router,prefix='/receipts',tags=['Receipts'])
app.include_router(customer.router,prefix='/customers',tags=['Customer'])
app.include_router(job_request.router,prefix='/job_requests',tags=['Job Requests'])
app.include_router(general.router,prefix='/general',tags=['General Utility'])
app.include_router(stock.router,prefix='/stock',tags=['Stock'])
app.include_router(pattern.router,prefix='/pattern',tags=['Pattern'])
app.include_router(material.router,prefix='/material',tags=['Material'])
app.include_router(delivery_notes.router,prefix='/delivery_notes',tags=['Delivery Notes'])
app.include_router(employee_time_logs.router,prefix='/employee_time_logs',tags=['Employee Time Logs'])




############### ENDPOINTS #####################



########## MAIN UTILITY CALLS ###############

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/ping", include_in_schema=True)
async def Ping():
    return "pong"

@app.get("/set_users", include_in_schema=True)
async def setUsers():   
    try:   
        res = await set_users()
        return "Done"
    except Exception as e:
        return {"error": str(e)}