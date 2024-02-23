from datetime import datetime
from typing import List
from infrastructure.entity.CardEntity import CardEntity

from flask import Flask
from infrastructure.entity.CardEntity import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask SQLAlchemy with the app

db.init_app(app) 
class QuizzCardServer:
    
     def findQuizzCardDay(self,date: datetime) -> List[CardEntity]:
        
      with app.app_context():
        card_entities =  CardEntity.query.filter_by(date_next_response = date).all()
         
      return card_entities

        