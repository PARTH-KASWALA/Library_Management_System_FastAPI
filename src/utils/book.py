import random
import uuid
from datetime import timedelta
import datetime

def generate_unique_id():
    return str(uuid.uuid4())

def calculate_due_date(borrow_date: datetime, days: int = 14):
    return borrow_date + timedelta(days=days)