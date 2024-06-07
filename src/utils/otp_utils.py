# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# # Email configuration
# sender_email = "parthkaswala95@gmail.com"
# receiver_email ="parthkaswala2004@gmail.com"
# password = "irnyitpcqjlebnmv"
# subject = "Your OTP Code"
# otp = "789798"
# message_text = f"Your OTP is {otp} which is valid for 1 minute"
# # Create the email message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# # Attach the message text
# message.attach(MIMEText(message_text, "plain"))
# # Send the email
# try:
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message.as_string())
#     print("Mail sent successfully")
#     server.quit()
# except Exception as e:
#     print(f"Failed to send email: {e}")




import random
from datetime import datetime, timedelta
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.models.models_Lib import OTP, User
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("EMAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("EMAIL_PASSWORD"),
    MAIL_FROM=os.getenv("EMAIL_FROM"),
    MAIL_PORT=int(os.getenv("EMAIL_PORT")),
    MAIL_SERVER=os.getenv("EMAIL_HOST"),
    MAIL_FROM_NAME=os.getenv("EMAIL_FROM_NAME"),
    MAIL_TLS=True,
    MAIL_SSL=False
)

def generate_otp():
    return str(random.randint(100000, 999999))

def save_otp_to_db(db: Session, user: User, otp: str):
    db_otp = OTP(otp=otp, user_id=user.id)
    db.add(db_otp)
    db.commit()
    db.refresh(db_otp)
    return db_otp

async def send_otp_email(email: str, otp: str):
    message = MessageSchema(
        subject="Your OTP Code",
        recipients=[email],
        body=f"Your OTP code is {otp}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
