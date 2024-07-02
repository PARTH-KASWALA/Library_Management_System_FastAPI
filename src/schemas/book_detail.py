
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

#------------------Book------------------------
class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    published_date: datetime
class Book(BookBase):
    created_at: datetime
    modified_at: datetime

class BookCreate(BaseModel):
    title: str
    author_id: str
    category_id: str
    isbn: str
    description: str
    published_date: datetime
    copies_available: int


#-------------Author Schemas----------------
class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    name: str
    bio: Optional[str] = None


class AuthorUpdate(AuthorBase):
    name: str
    bio: Optional[str] = None


class Author(AuthorBase):
    created_at: datetime
    modified_at: datetime



#------------------Category------------------------


class CategoryBase(BaseModel):
    name: str
    description: str
    id: str
    created_at: datetime
    modified_at: datetime

class CategoryCreate(CategoryBase):
    id : str

class CategoryUpdate(CategoryBase):
    id : str
    name : str
    description: str


class Category(CategoryBase):
    id: str
    name: str
    description: str

 



#------------------Borrowing------------------------


class Borrowing(BaseModel):
    user_id: str
    book_id: str
    borrow_date: datetime
    return_date: Optional[datetime] = None

class BorrowingCreate(BaseModel):
    user_id: str
    book_id: str
    borrow_date: datetime
    return_date: Optional[datetime] = None




#------------------Reservation------------------------

class ReservationBase(BaseModel):
    user_id: str
    book_id: str
    reservation_date: datetime
    
class ReservationCreate(BaseModel):
    reservation_date: datetime
    user_id: str
    book_id: str

