from datetime import datetime,timedelta
from fastapi import HTTPException,status,Security
from dotenv import load_dotenv
import os
from jose import jwt,JWTError
load_dotenv()
SECRET_KEY = str(os.environ.get("SECRET_KEY"))
ALGORITHM = str(os.environ.get("ALGORITHM"))

def get_encode_token(id):
    payload = {
        "id" : id,
        "exp" : datetime.now() + timedelta(minutes=10)
    }
    access_token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    print(type(access_token))
    return access_token

def decode_token_id(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("id")
        if not id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )



def get_token_login(first_name,last_name,password):
    payload = {
        "first_name": first_name,
        "last_name" : last_name,
        "password": password,
        "exp": datetime.utcnow() + timedelta(minutes=10),
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(type(access_token))
    return access_token




def decode_token_first_name(token):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        first_name = payload.get("first_name")
        if not first_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return first_name
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )

def decode_token_password(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        password = payload.get("password")
        if not password:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token"
            )
        return password
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )



