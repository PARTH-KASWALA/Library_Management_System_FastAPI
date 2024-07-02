from fastapi import FastAPI
from src.routers.User_Routers import user,Otp
from src.routers.Book_Routers import book_router
from src.routers.Borrowing_Routers import borrowing_router
from src.routers.Reservation_Routers import reservation_router
from src.routers.Author_Routers import author_router
from src.routers.Category_Routers import category_router
app = FastAPI()

app.include_router(user)
app.include_router(Otp)
app.include_router(user)
app.include_router(book_router)
app.include_router(borrowing_router)
app.include_router(reservation_router)
app.include_router(author_router)
app.include_router(category_router)
