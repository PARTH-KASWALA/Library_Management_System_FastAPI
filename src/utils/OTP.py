import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Email configuration
sender_email = "kinalramani14@gmail.com"
receiver_email = "neelmakvana168@gmail.com"
password = "irnyitpcqjlebnmv"
subject = "Your OTP Code"
otp = "789798"
message_text = f"Your OTP is {otp} which is valid for 1 minute"
# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# Attach the message text
message.attach(MIMEText(message_text, "plain"))
# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Mail sent successfully")
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")