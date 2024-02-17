from  infrastructure.entity.CardEntity import CardEntity , db

class AnswerCardServer:

    def getCardById(self,cardId :  str) ->  CardEntity :
        return CardEntity.query.get(cardId)
    
    def updateCard(self, cardEntity : CardEntity):
        db.session.commit()