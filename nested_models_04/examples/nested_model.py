from typing import List, Optional
from pydantic import BaseModel #type: ignore

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    addresses: List[Address]  # Changed to List[Address] for multiple addresses

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(
    street="123 Main St",
    city="Anytown",
    zipcode="12345"
)

user = User(
    id=1,
    name="John Doe",
    email="john@example.com",
    addresses=address
)

comment = Comment(
    id=1,
    content="This is a comment.",
    replies=[
        Comment(
            id=2,
            content="This is a reply."
        ),
        Comment(
            id=3,
            content="This is another reply.",
            replies=[
                Comment(
                    id=4,
                    content="This is a nested reply."
                )
            ]
        )
    ]
)