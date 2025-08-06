from pydantic import BaseModel
from datetime import time

class EmployeeTimeLog(BaseModel):
    employee_time_log_id: int
    clock_in: time
    clock_out: time
    employee_id: int