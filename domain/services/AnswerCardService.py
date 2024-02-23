from domain.models.Card import Card
from domain.models.Category import Category
from infrastructure.repository.AnswerCardServer import AnswerCardServer


class AnswerCardService:

    def __init__(self) -> None:
        self.answerCardServer = AnswerCardServer()

    def correctAnswer(self, category):
        next_category = {
            "FIRST": "SECOND",
            "SECOND":"THIRD",
            "THIRD": "FOURTH",
            "FOURTH":"FIFTH",
            "FIFTH": "SIXTH",
            "SIXTH": "SEVENTH",
            "SEVENTH": "DONE"
        }.get(category)
        if next_category:
            return next_category
        

          
    def wrongAnswer(self, category : str):
        category = "FIRST"
        return category
    
    def answer_card(self, card_id: str, is_correct: bool):
        card_entity = self.answerCardServer.getCardById(card_id)
        if not card_entity:
            return 404
        
        if is_correct:
            card_entity.category = self.correctAnswer(card_entity.category)
            self.answerCardServer.updateCard(card_entity)
            return 204

         
        else:
            card_entity.category = self.wrongAnswer(card_entity.category)   
            self.answerCardServer.updateCard(card_entity)
            return 400
            
       
    

