from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


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
