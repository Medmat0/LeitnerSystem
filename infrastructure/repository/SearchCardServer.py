from infrastructure.entity.CardEntity import CardEntity
from typing import List
from flask import Flask
from infrastructure.entity.CardEntity import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask SQLAlchemy with the app

db.init_app(app) 

class SearchCardServer: 

    def findByTag(self, tag: str) -> List[CardEntity]:
        with app.app_context():
            if tag:
                card_entities = CardEntity.query.filter_by(tag=tag).all()
            else:
                card_entities = CardEntity.query.all()
            return card_entities
    
    def getAllCard(self) -> List[CardEntity]:
         with app.app_context():
            card_entities = CardEntity.query.all()
            return card_entities


