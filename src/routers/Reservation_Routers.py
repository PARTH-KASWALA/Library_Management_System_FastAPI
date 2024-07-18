from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.Database import SessionLocal
from src.models.Reservation import Reservation
from src.schemas.Book_Detail import  ReservationCreate, ReservationBase
from typing import List


reservation_router = APIRouter(tags=["Reservation"])
db = SessionLocal()


# ----------------------------------------------create_reservation------------------------------------------------------
@reservation_router.post("/create_reservation/", response_model=ReservationBase)
def create_reservation(reservation: ReservationCreate):
    new_reservation = Reservation(
        user_id=reservation.user_id,
        book_id=reservation.book_id,
        reservation_date=reservation.reservation_date
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation




# ----------------------------------------------get_reservations------------------------------------------------------
@reservation_router.get("/reservations/", response_model=List[ReservationBase])
def get_reservations():
    return db.query(Reservation).all()

