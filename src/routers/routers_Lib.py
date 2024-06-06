from fastapi import FastAPI,HTTPException,APIRouter,Depends,Header
from database.database import SessionLocal
from src.models.models_Lib import User
from src.schemas.schemas_Lib import  UserBase,Usercreate,UserUpdate,UserPasswordReset
import uuid
from passlib.context import CryptContext
from typing import List
# from src.utils.token import get_encode_token,get_token_login,decode_token_emp_id,decode_token_emp_name,decode_token_password
# from logs.log_config import logger
from jose import JWTError, jwt


# from passlib.context import CryptContext
# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from typing import Optional
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from database.database import SessionLocal
# from src.models.models_Lib import User
# from src.schemas.schemas_Lib import TokenData
# from dotenv import load_dotenv
# import os


router = APIRouter()
db=SessionLocal()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#-------------------------User create ----------------------------


@router.post("/users create /", response_model=UserBase)
def add_user(User:Usercreate):
    new_Create_User = User(
        first_name = User.first_name,
        last_name = User.last_name,
        email = User.email,
        password = User.password
    )
    db.add(new_Create_User)
    db.commit()
    return new_Create_User



