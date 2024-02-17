from domain.models.Card import Card
from client.dto.ClientCart import ClientCard

def map_domain_card_to_client_card (card : Card) -> ClientCard:
   clientCard = ClientCard
   clientCard.id = card.id
   clientCard.answer = card.answer
   clientCard.category = card.category
   clientCard.question = card.question
   clientCard.tags = card.tags
   return clientCard