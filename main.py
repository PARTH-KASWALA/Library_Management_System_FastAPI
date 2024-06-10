from fastapi import FastAPI
from src.routers.routers_Lib import router
from src.routers.otp import Otp
app = FastAPI()

app.include_router(router)
app.include_router(Otp)

   