from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

user = User(
    id = 1,
    name = 'Chintu',
    email = 'chintu@example.com',
    createdAt = datetime(2024, 3, 15, 14, 30),
    address = Address(
        street= "something",
        city= "Odisha",
        zipcode = "00000"
    ),
    tags = ["premium", "subscriber"]
)

python_dict = user.model_dump()
print(python_dict)
print("=========================")
json_str = user.model_dump_json()
print(json_str)