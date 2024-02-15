from models.Card import Card
from models.Category import Category
from infrastructure.repository.AnswerCardServer import AnswerCardServer


class AnswerCard:

    def __init__(self) -> None:
        self.answerCardServer = AnswerCardServer

    def correct_answer(self, cardEntity) -> None:
        if cardEntity.category == Category.SEVENTH:
            cardEntity.category = Category.DONE
        elif cardEntity.category != Category.SEVENTH:
            cardEntity.category = Category(cardEntity.category.value + 1)

    def wrong_answer(self, cardEntity) -> None:
        cardEntity.category = Category.FIRST
    
    def answer_card(self, cardId: str, is_correct: bool):
        cardEntity = self.answerCardServer.getCardById(cardId)
        if not cardEntity:
            raise ValueError("NOT FOUND")
        
        if is_correct:
            card = self.correctAnswer(cardEntity)
        else:
            card = self.wrongAnswer(cardEntity)
        self.answerCardServer.updateCard(cardEntity)
    
