
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