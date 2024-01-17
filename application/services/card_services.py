from datetime import datetime, timedelta
from domain.models.cardmodel.card import Card 
from domain.models.cardmodel.validation_card import ValidationCard 
from domain.repository.cardRepository import CardRepository
from typing import List

class CardService:

    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository



    def create_card(self):
        validcard = ValidationCard()
        card = self.card_repository.add_card(validcard)
        card.update_next_review_date()  # Initialiser la date de révision lors de la création
        
        return card



    def get_cards(self, tags: List[str] = None) -> List[Card]:
        return self.card_repository.get_cards(tags)