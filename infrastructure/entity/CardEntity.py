from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask

db = SQLAlchemy()

class CardEntity(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    date_next_response = db.Column(db.Date, default=datetime.now())