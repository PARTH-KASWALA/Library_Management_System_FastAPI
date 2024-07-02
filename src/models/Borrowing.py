from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, JSON,Text,Float
import uuid
from datetime import datetime, timedelta
from database.Database import Base



# ----------------------------------------------Borrowing Table------------------------------------------------------
class Borrowing(Base):
    __tablename__ = "borrowings"

    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(100), ForeignKey('books.id'), nullable=False)
    borrow_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime, nullable=True)
    due_date = Column(DateTime, default=datetime.now() + timedelta(days=20))
     
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
