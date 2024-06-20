
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, JSON,Text
import uuid
from database.database import Base
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    mobile_no = Column(String(50), nullable=False)
    password = Column(String(80), nullable=False)
    bio = Column(String(100), nullable=False)
    role = Column(String(100), default=False)
    address = Column(String(200), default=False)
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_verified = Column(Boolean, default=False)




# class OTP(Base):
#     __tablename__ = "otps"

#     id = Column(Integer, primary_key=True, default=str(uuid.uuid4()))
#     otp = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     created_at = Column(DateTime, default=datetime.now)
#     user = relationship("User", back_populates="otps")

# User.otps = relationship("OTP", order_by=OTP.id, back_populates="user")






class OTP(Base):
    __tablename__ = "otp"
    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(50), nullable=False)
    otp = Column(String(6), nullable=False)
    expired_time = Column(DateTime, default=lambda: datetime.now() + timedelta(minutes=1))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)




class Author(Base):
    __tablename__ = "authors"
    
    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    books = relationship("Book", back_populates="author")

class Category(Base):
    __tablename__ = "categories"

    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    books = relationship("Book", back_populates="category")



# class Book(Base):
#     __tablename__ = "books"

#     id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
#     title = Column(String(100), nullable=False)
#     author_id = Column(String(50), ForeignKey('author.id'), nullable=False)
#     category_id = Column(String(50), ForeignKey('category.id'), nullable=False)
#     isbn = Column(String(13), unique=True, nullable=False)
#     description = Column(Text, nullable=True)
#     published_date = Column(Date, nullable=False)
#     copies_available = Column(Integer, nullable=False, default=1)
#     created_at = Column(DateTime, default=datetime.now)
#     modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#     # Relationships
#     author = relationship("Author", back_populates="books")
#     category = relationship("Category", back_populates="books")


class Book(Base):
    __tablename__ = "books"
    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(100), nullable=False)
    author_id = Column(String(50), ForeignKey('authors.id'))
    category_id = Column(String(50), ForeignKey('categories.id'))
    isbn = Column(String(13), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    published_date = Column(Date, nullable=False)
    copies_available = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    author = relationship("Author", back_populates="books")
    category = relationship("Category", back_populates="books")
    # borrowings = relationship("Borrowing", back_populates="book")

# class Borrowing(Base):
#     __tablename__ = "borrowings"
#     id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
#     user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
#     book_id = Column(String(50), ForeignKey('books.id'), nullable=False)
#     borrow_date = Column(Date, nullable=False, default=datetime.now)
#     due_date = Column(Date, nullable=False)
#     is_returned = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.now)
#     modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#     user = relationship("User", back_populates="borrowings")
#     book = relationship("Book", back_populates="borrowings")

class Borrowing(Base):
    __tablename__ = "borrowings"

    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(50), ForeignKey(' books.id'), nullable=False)
    borrow_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime, nullable=True)
    due_date = Column(DateTime, default=lambda: datetime.now() + timedelta(days=14))
    is_returned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(50), ForeignKey('books.id'), nullable=False)
    reservation_date = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)