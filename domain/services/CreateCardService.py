from domain.models.Category import  Category
from domain.models.Card import Card
from domain.models.CardUserData import CardUserData
from domain.models.CardId import CardId
import uuid
from infrastructure.mapper.MapCard import map_card_to_server
from infrastructure.repository.CreateCardServer import CreateCardRepository


 # to verify that all champ is not empty
def isEmpty(input : str):
    if(input.strip()):
        return False
    else:
        return True


class CreateCardService:
     
   
    def CreateCard(self,cardUserData : CardUserData) -> Card:
        if isEmpty(cardUserData.question) or  isEmpty(cardUserData.answer):
            ValueError("Make sure to fill all champs please !!")
        else:
            randomId = str(uuid.uuid4())
            newCard = Card(
                        id = CardId(id = randomId),
                        category = Category.FIRST,
                        question=cardUserData.question,
                        answer=cardUserData.answer,
                        tag=cardUserData.tag
                        )
            
            # Save card in infra db 
            cardEntity = map_card_to_server(newCard)
            createCardRepository = CreateCardRepository 
            createCardRepository.save_card(cardEntity)  
            return  newCard
        
        
    