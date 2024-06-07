from fastapi import FastAPI
from src.routers.routers_Lib import router

app = FastAPI()

app.include_router(router)


   