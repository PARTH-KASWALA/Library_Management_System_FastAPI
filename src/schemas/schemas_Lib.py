
from pydantic import BaseModel,EmailStr
from typing import List,Optional
from datetime import datetime,date

class UserBase(BaseModel):
    username: str
    email: str
    bio: Optional[str] = None

class UserCreate(BaseModel):
    first_name:str
    last_name:str
    password: str

class Users(BaseModel):
   
    first_name :str
    last_name :str
    username :str
    email :str
    mobile_no :str
    password :str
    bio :str
    role :str
    address :str

class UserUpdate(BaseModel):
    username:str
    password:str

class UsersPatch(BaseModel):
    first_name :Optional[str]=None
    last_name :Optional[str]=None
    username :Optional[str]=None
    email :Optional[str]=None
    mobile_no :Optional[str]=None
    password :Optional[str]=None
    bio :Optional[str]=None
    role :Optional[str]=None
    address :Optional[str]=None



class OTPRequest(BaseModel):
    email: EmailStr
class OTPVerify(BaseModel):
    email: EmailStr
    otp: str











