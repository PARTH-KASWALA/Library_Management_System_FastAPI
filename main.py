from fastapi import FastAPI
from src.routers import routers_Lib

app = FastAPI

app.include_router(routers_Lib)
