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

# Initialise Flask SQLAlchemy avec l'application

db.init_app(app) 


def isEmpty(input : str):
    """
    Vérifie si une chaîne de caractères est vide.

    Args:
        input (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si la chaîne est vide, sinon False.
    """

    if(input.strip()):
        return False
    else:
        return True


class CreateCardService:
     
    def CreateCard(self,card_userdata : CardUserData) -> Card:
        """
        Crée une nouvelle carte à partir des données utilisateur.

        Args:
            card_userdata (CardUserData): Les données utilisateur pour créer la carte.

        Returns:
            Card: La carte créée.
        
        Raises:
            ValueError: Si l'une des données obligatoires est manquante.
        """
        
        if isEmpty(card_userdata.question) or  isEmpty(card_userdata.answer):
            raise ValueError("Make sure to fill all champs please !!")
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
            
