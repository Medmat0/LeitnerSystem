from abc import ABC, abstractmethod
from typing import List
from  domain.models.card import Card
from  domain.models.userInput import UserInput


class CardServices(ABC):  

    def __init__(self):
        self.cards = []


    @abstractmethod
    def add_card( userInput :UserInput ) -> Card:
         return  Card(
            question=userInput.question,
            answer=userInput.answer,
            tags=userInput.tags
        )
            

    @abstractmethod
    def get_cards(self, tags: List[str] = None) -> List[Card]:
        if tags:
            return [card for card in self.cards if any(tag in card.tags for tag in tags)]
        else:
            return self.cards
        
