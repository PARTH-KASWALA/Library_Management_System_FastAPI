from fastapi import FastAPI
from src.routers.user import user,Otp
# from src.routers.otp import Otp
from src.routers.book import book_router
from src.routers.borrowing import borrowing_router
from src.routers.reservation import reservation_router
app = FastAPI()

app.include_router(user)
app.include_router(Otp)
app.include_router(user)
app.include_router(book_router)
app.include_router(borrowing_router)
app.include_router(reservation_router)
