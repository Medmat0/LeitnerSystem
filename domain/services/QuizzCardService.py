from datetime import datetime
from domain.models.Card import Card
from typing import List
from infrastructure.repository.QuizzCardServer import QuizzCardServer
from infrastructure.mapper.MapCard import map_card_entity_to_domain

class QuizzCardService:

    def __init__(self,quizzCardServer : QuizzCardServer ) -> None:
        self.quizzCardServer = quizzCardServer    
        pass

    def getQuizDay(self,day: str = None) -> datetime:
        if day:
            quiz_date = datetime.strptime(day, '%Y-%m-%d')
        else:
            quiz_date = datetime.now().date()
        return quiz_date

    def fetch_cards_for_quiz(self,quiz_date: datetime) -> List[Card]:
        card_entities = self.find_by_date_or_current(quiz_date)
        cards = map_card_entity_to_domain(card_entities)
        return cards