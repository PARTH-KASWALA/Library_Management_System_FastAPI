from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    email: EmailStr


class Usercreate(UserBase):
    first_name: str
    last_name: str
    password : str
    email : str

class UserUpdate(BaseModel):
    first_name: str
    last_name: str


class UserPasswordReset(BaseModel):
    email: EmailStr
    new_password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None


class OTPRequest(BaseModel):
    email: EmailStr

class OTPVerify(BaseModel):
    email: EmailStr
    otp: str