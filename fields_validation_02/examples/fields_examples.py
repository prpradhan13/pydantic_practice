from pydantic import BaseModel
from typing import List, Optional, Dict

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantites: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
