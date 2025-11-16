from pydantic import BaseModel, Field
from typing import Optional

# TODO: Create Employee model:
# - id: integer
# - name: string (minimum length 3)
# - department: optional string (default to General)
# - salary: float (must be greater than 30000)

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        json_schema_extra={
            "minLength": 3,
            "max_length": 50,
            "description": "Name must be at least 3 characters long",
            "example": "John Doe"
        },
        )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        json_schema_extra={
            "gt": 30000, 
            "description": "Employee salary",
            "example": 50000.0
        },
        ) 
    
emp_01 = {
    "id": 1,
    "name": "Alice Smith",
    "department": "Engineering",
    "salary": 75000.0
}

emp_02 = {
    "id": 2,
    "name": "Bob",
    "salary": 28000.0
}

employee_1 = Employee(**emp_01)
print(employee_1)