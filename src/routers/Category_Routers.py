from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from src.models.Category import Category
from database.Database import SessionLocal
from src.schemas.Book_Detail import CategoryBase, CategoryUpdate,CategoryCreate
import uuid


category_router = APIRouter(tags=["Category"])
db = SessionLocal()


# ----------------------------------------------create_category------------------------------------------------------
@category_router.post("/create_category", response_model=CategoryCreate)
def create_category(category: CategoryBase):
    db_category = Category(id=str(uuid.uuid4()), name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    db.close()
    return db_category



# ----------------------------------------------update_category------------------------------------------------------
@category_router.put("/update_category", response_model=CategoryBase)
def update_category(category_id: str, category: CategoryUpdate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        db.close()
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.commit()
    db.refresh(db_category)
    db.close()
    return db_category




# ----------------------------------------------delete_category------------------------------------------------------
@category_router.delete("/delete_category")
def delete_category(category_id: str):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(db_category)
    db.commit()
    return {"detail": "Category deleted"}



