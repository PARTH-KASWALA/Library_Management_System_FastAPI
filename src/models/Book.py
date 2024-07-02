from sqlalchemy import Column, Integer, String,ForeignKey, Date
import uuid
from database.Database import Base
from src.models.Author import Author
from src.models.Category import Category


# ----------------------------------------------Book Table------------------------------------------------------
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    title = Column(String(50), nullable=False)
    author_id = Column(String(100), ForeignKey('authors.id'), nullable=False)
    category_id = Column(String(100), ForeignKey('categories.id'), nullable=False)
    isbn = Column(String(50),nullable=False)
    description = Column(String(50))
    published_date = Column(Date)
    copies_available = Column(Integer, default=0)

"""
It need cerate or modified Column so add it.
"""
    # created_at = Column(DateTime, default=datetime.now)
    # modified_at = Column(DateTime, default=datetime.now,onupdate=datetime.now)




