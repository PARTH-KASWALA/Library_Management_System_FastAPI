from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.models.Book import Book
from src.schemas.Book_Detail import BookCreate
from database.Database import SessionLocal
import uuid


book_router = APIRouter(tags=["Books"])
db = SessionLocal()


# ----------------------------------------------create_book------------------------------------------------------
@book_router.post("/create_book/")
def create_book(book: BookCreate):
        db_book = Book(
            id = str(uuid.uuid4()),
            title=book.title,
            author_id=book.author_id,
            category_id=book.category_id,
            isbn=book.isbn,
            description=book.description,
            published_date=book.published_date,
            copies_available=book.copies_available,
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book




