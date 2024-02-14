from models.Category import  Category
from models.Card import Card
from models.CardUserData import CardUserData
from models.CardId import CardId
import uuid



 # to verify that all champ is not empty
def isEmpty(input : str):
    if(input.strip()):
        return False
    else:
        return True


class CreateCardService:
     
   
    def CreateCard(cardUserData : CardUserData) -> Card:
        if isEmpty(cardUserData.question) or  isEmpty(cardUserData.answer):
            ValueError("Make sure to fill all champs please !!")
        else:
            randomId = str(uuid.uuid4())
            return Card(
                        id = CardId(id = randomId),
                        category = Category.FIRST,
                        question=cardUserData.question,
                        answer=cardUserData.answer,
                        tag=cardUserData.tag
                        )
        
        
    