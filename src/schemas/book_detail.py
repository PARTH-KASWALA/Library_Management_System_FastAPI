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



class BorrowingBase(BaseModel):
    user_id: str
    book_id: str

class BorrowingCreate(BorrowingBase):
    pass

class Borrowing(BorrowingBase):
    id: str
    borrow_date: datetime
    return_date: Optional[datetime] = None
    due_date: datetime
    is_returned: bool
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True




class ReservationBase(BaseModel):
    user_id: str
    book_id: str

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: str
    reservation_date: datetime
    is_active: bool
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True