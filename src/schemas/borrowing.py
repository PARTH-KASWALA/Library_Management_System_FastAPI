from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


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