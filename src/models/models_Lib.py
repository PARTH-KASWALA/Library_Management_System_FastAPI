
from sqlalchemy import Column,String, Boolean, DateTime
import uuid
from datetime import datetime
from database.Database import Base




# ----------------------------------------------User Table------------------------------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    mobile_no = Column(String(50),unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    bio = Column(String(100), nullable=False)
    role = Column(String(100), default=False)
    address = Column(String(200), default=False)
    
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_verified = Column(Boolean, default=False)
















