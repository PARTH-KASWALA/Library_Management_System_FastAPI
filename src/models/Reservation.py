from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, JSON,Text
import uuid
from datetime import datetime
from database.Database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(100), ForeignKey('books.id'), nullable=False)
    reservation_date = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
