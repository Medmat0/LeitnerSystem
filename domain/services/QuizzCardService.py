from datetime import datetime
from domain.models.Card import Card
from typing import List
from infrastructure.repository.QuizzCardServer import QuizzCardServer
from infrastructure.mapper.MapCard import map_card_entity_to_domain

class QuizzCardService:

    def fetch_cards_for_quiz(self,quiz_date: datetime) -> List[Card]:
        quizz_card_server = QuizzCardServer()
        card_entities = quizz_card_server.findQuizzCardDay(quiz_date)
        cards = [map_card_entity_to_domain(card_entitie) for card_entitie in card_entities]
        return cards
    

