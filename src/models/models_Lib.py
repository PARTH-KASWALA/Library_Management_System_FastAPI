from sqlalchemy import  Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from datetime import datetime
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,default=str(uuid.uuid4())) #autoincrement=True
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String, unique=True,nullable=False)
    password = Column(String, nullable=False)
    is_active=Column(Boolean,default=True)
    is_deleted=Column(Boolean,default=False)
    created_at=Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)




class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, default=str(uuid.uuid4()))
    otp = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    user = relationship("User", back_populates="otps")

User.otps = relationship("OTP", order_by=OTP.id, back_populates="user")