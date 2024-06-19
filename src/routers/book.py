from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.models.models_Lib import Book, Borrowing, Reservation, User
from src.schemas.schemas_Lib import BookCreate, Book, BorrowingCreate, Borrowing, ReservationCreate, Reservation
from src.utils.token import decode_token_user_id
import datetime
from typing import List


book_router = APIRouter()
borrowing_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Book Endpoints
@book_router.post("/books/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@book_router.get("/books/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Borrowing Endpoints
@borrowing_router.post("/borrowings/", response_model=Borrowing)
def create_borrowing(borrowing: BorrowingCreate, db: Session = Depends(get_db)):
    db_borrowing = Borrowing(**borrowing.dict())
    db.add(db_borrowing)
    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing

@borrowing_router.get("/borrowings/", response_model=List[Borrowing])
def get_borrowings(db: Session = Depends(get_db)):
    return db.query(Borrowing).all()

@borrowing_router.put("/borrowings/return/{borrowing_id}", response_model=Borrowing)
def return_book(borrowing_id: str, db: Session = Depends(get_db)):
    db_borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    if not db_borrowing:
        raise HTTPException(status_code=404, detail="Borrowing record not found")
    db_borrowing.return_date = datetime.now()
    db_borrowing.is_returned = True
    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing

