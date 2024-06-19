from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    published_date: date

class BookCreate(BookBase):
    copies_available: int

class Book(BookBase):
    id: str
    copies_available: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True