from domain.models.Category import  Category
from domain.models.Card import Card
from domain.models.CardUserData import CardUserData
from domain.models.CardId import CardId
import uuid
from infrastructure.mapper.MapCard import map_card_to_server
from infrastructure.mapper.MapCard import map_card_entity_to_domain
from infrastructure.repository.CreateCardServer import CreateCardRepository
from flask import Flask
from infrastructure.entity.CardEntity import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask SQLAlchemy with the app

db.init_app(app) 
 # to verify that all champ is not empty
def isEmpty(input : str):
    if(input.strip()):
        return False
    else:
        return True


class CreateCardService:
     
   
    def CreateCard(self,card_userdata : CardUserData) -> Card:
        if isEmpty(card_userdata.question) or  isEmpty(card_userdata.answer):
            ValueError("Make sure to fill all champs please !!")
        else:
            randomId = str(uuid.uuid4())
            newCard = Card(
                        id =  randomId,
                        category= Category.FIRST,
                        question=card_userdata.question,
                        answer  =card_userdata.answer,
                        tags    =card_userdata.tag
                        )
            
            # Save card in infra db 
            card_entity = map_card_to_server(newCard)
            with app.app_context():
                db.create_all()
                create_card_repository = CreateCardRepository() 
                create_card_repository.save_card(card_entity)  
                card = map_card_entity_to_domain(card_entity)
            
            return  card
            
