from app import db
from datetime import datetime

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(30))
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.now)