from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.models.models_Lib import Book, Borrowing, Reservation, User
from src.schemas.book_detail import BookCreate, Book, BorrowingCreate, Borrowing, ReservationCreate, Reservation
from src.utils.token import decode_token_user_id
# import datetime
from typing import List

reservation_router = APIRouter()

def get_db():
    return SessionLocal()
# Reservation Endpoints
@reservation_router.post("/reservations/", response_model=Reservation)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@reservation_router.get("/reservations/", response_model=List[Reservation])
def get_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()

@reservation_router.put("/reservations/cancel/{reservation_id}", response_model=Reservation)
def cancel_reservation(reservation_id: str, db: Session = Depends(get_db)):
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db_reservation.is_active = False
    db.commit()
    db.refresh(db_reservation)
    return db_reservation
