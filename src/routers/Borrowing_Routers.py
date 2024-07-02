from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.Database import SessionLocal
from src.models.Borrowing import  Borrowing
from src.schemas.Book_Detail import BorrowingCreate
from typing import List
import datetime 
from datetime import timedelta
from typing import Optional

borrowing_router = APIRouter()
db = SessionLocal()


# def calculate_penalty(due_date: datetime.datetime, return_date: Optional[datetime.datetime]) -> float:
#     if return_date and return_date > due_date:
#         days_overdue = (return_date - due_date).days
#         return days_overdue * 1.0  # Assuming a penalty of 1.0 per day overdue
#     return 0.0


# @borrowing_router.post("/create_borrowing", response_model=BorrowingCreate)
# def create_borrowing(borrowing: BorrowingCreate):
#     new_borrowing = Borrowing(
#         user_id=borrowing.user_id,
#         book_id=borrowing.book_id,
#         borrow_date=borrowing.borrow_date,
#         return_date=borrowing.return_date,
#         penalty=calculate_penalty(borrowing.borrow_date + timedelta(days=20), borrowing.return_date)
#     )
#     db.add(new_borrowing)
#     db.commit()
#     db.refresh(new_borrowing)
#     return new_borrowing



# @borrowing_router.get("/get_borrowings/", response_model=List[BorrowingCreate])
# def get_borrowings():
#     borrowings = db.query(Borrowing).all()
#     for borrowing in borrowings:
#         borrowing.penalty = calculate_penalty(borrowing.due_date, borrowing.return_date)
#     return borrowings



@borrowing_router.post("/create_borrowing", response_model=BorrowingCreate)
def create_borrowing(borrowing: BorrowingCreate):
    new_borrowing = Borrowing(
        user_id=borrowing.user_id,
        book_id=borrowing.book_id,
        borrow_date=borrowing.borrow_date,
        return_date=borrowing.return_date
    )
    db.add(new_borrowing)
    db.commit()
    db.refresh(new_borrowing)
    return new_borrowing



@borrowing_router.get("/get_borrowings/", response_model=List[BorrowingCreate])
def get_borrowings():
    return db.query(Borrowing).all()












# @borrowing_router.put("/borrowings/return/{borrowing_id}", response_model=BorrowingCreate)
# def return_book(borrowing_id: str):
#     db_borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
#     if not db_borrowing:
#         raise HTTPException(status_code=404, detail="Borrowing record not found")
#     db_borrowing.return_date = datetime.now()
#     db.commit()
#     db.refresh(db_borrowing)
#     return db_borrowing

