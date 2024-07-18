from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.Author import Author
from database.Database import SessionLocal
from datetime import datetime
from src.schemas.Book_Detail import  AuthorUpdate ,AuthorBase


author_router = APIRouter(tags=["Author"])
db = SessionLocal()


# ----------------------------------------------create_author------------------------------------------------------
@author_router.post("/create_author", response_model=AuthorBase)
def create_author(author: AuthorBase):
    db_author = Author(
        name=author.name,
        bio=author.bio,
        created_at=datetime.now(),
        modified_at=datetime.now()
        )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author




# ----------------------------------------------update_author------------------------------------------------------
@author_router.put("/update_author", response_model=AuthorBase)
def update_author(author_id: str, author: AuthorUpdate):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.commit()
    db.refresh(db_author)
    return db_author



# ----------------------------------------------delete_author------------------------------------------------------
@author_router.delete("/delete_author")
def delete_author(author_id: str):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    db.delete(db_author)
    db.commit()
    return {"detail": "Author deleted"}











# @author_router.get("/read_author", response_model=Author)
# def read_author(author_id: str):
#     db_author = db.query(Author).filter(Author.id == author_id).first()
#     db.close()
#     if db_author is None:
#         raise HTTPException(status_code=404, detail="Author not found")
#     return db_author



# @author_router.put("/update_author", response_model=AuthorSchema)
# def update_author(author_id: str, author: AuthorUpdate):
#     db_author = db.query(Author).filter(Author.id == author_id).first()
#     if db_author is None:
#         db.close()
#         raise HTTPException(status_code=404, detail="Author not found")
    
    
#     db.commit()
#     db.refresh(db_author)
#     db.close()
#     return db_author



# @author_router.delete("/delete_author")
# def delete_author(author_id: str):
#     db_author = db.query(Author).filter(Author.id == author_id).first()
#     if db_author is None:
#         db.close()
#         raise HTTPException(status_code=404, detail="Author not found")
    
#     db.delete(db_author)
#     db.commit()
#     db.close()
#     return {"detail": "Author deleted"}
