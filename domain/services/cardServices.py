from abc import ABC, abstractmethod
from typing import List
from  domain.models.card import Card
from  domain.models.validation_card import ValidationCard


class CardRepository(ABC):  

    def __init__(self):
        self.cards = []


    @abstractmethod
    def add_card( valid_card :ValidationCard ) -> Card:
         return  Card(
            question=valid_card.question,
            answer=valid_card.answer,
            tags=valid_card.tags
        )
            

    @abstractmethod
    def get_cards(self, tags: List[str] = None) -> List[Card]:
        if tags:
            return [card for card in self.cards if any(tag in card.tags for tag in tags)]
        else:
            return self.cards
        
