from  infrastructure.entity.CardEntity import CardEntity , db
from flask import Flask

from infrastructure.entity.CardEntity import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask SQLAlchemy with the app

db.init_app(app) 


class AnswerCardServer:

    def getCardById(self,cardId :  str) ->  CardEntity :
        with app.app_context():
            return CardEntity.query.get(cardId)
    
    def updateCard(self, cardEntity : CardEntity):
        with app.app_context():
         db.session.add(cardEntity)
         db.session.commit()

