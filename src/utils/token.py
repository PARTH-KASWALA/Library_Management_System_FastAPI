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
        "emp_id" : id,
        "exp" : datetime.now() + timedelta(minutes=10)
    }
    access_token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    print(type(access_token))
    return access_token

def decode_token_emp_id(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        emp_id = payload.get("emp_id")
        if not emp_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return emp_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )



def get_token_login(emp_name,password):
    payload = {
        "emp_name": emp_name,
        "emp_password": password,
        "exp": datetime.utcnow() + timedelta(minutes=10),
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(type(access_token))
    return access_token




def decode_token_emp_name(token):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        emp_name = payload.get("emp_name")
        if not emp_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return emp_name
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
        
def decode_token_password(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        password = payload.get("emp_password")
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



