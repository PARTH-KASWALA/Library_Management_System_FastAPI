from fastapi import FastAPI
from src.routers.user import user,Otp
# from src.routers.otp import Otp
app = FastAPI()

app.include_router(user)
app.include_router(Otp)

