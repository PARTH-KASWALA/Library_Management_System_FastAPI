# src/routers/book.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.models.models_Lib import Book
from src.schemas.book_detail import BookCreate, Book as BookSchema
from datetime import datetime
from typing import List

book_router = APIRouter()

# Function to create a new database session
def get_db():
    return SessionLocal()

# Book Endpoints
@book_router.post("/books/", response_model=BookSchema)
def create_book(book: BookCreate):
    db = get_db()
    try:
        db_book = Book(
            title=book.title,
            author_id=book.author_id,
            category_id=book.category_id,
            isbn=book.isbn,
            description=book.description,
            published_date=book.published_date,
            copies_available=book.copies_available,
            created_at=datetime.now(),
            modified_at=datetime.now()
        )
        db.add(db_book)
        db.commit()
        # db.refresh(db_book)
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@book_router.get("/books/", response_model=List[BookSchema])
def get_books():
    db = get_db()
    try:
        return db.query(Book).all()
    finally:
        db.close()