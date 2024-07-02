from sqlalchemy import Column,String,DateTime
import uuid
from datetime import datetime
from database.Database import Base



class Category(Base):
    __tablename__ = "categories"

    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    description = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    