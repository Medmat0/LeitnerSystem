from domain.models.Card import Card
from client.dto.ClientCart import ClientCard
from typing import Dict
from domain.models.CardUserData import CardUserData


def map_domain_card_to_client_card (card : Card) -> ClientCard:
   client_card = ClientCard
   client_card.id = card.id
   client_card.answer = card.answer
   client_card.category = card.category
   client_card.question = card.question
   client_card.tags = card.tags
   return client_card


def serialize_client_card(client_card : ClientCard) :
   
      return {
            'id': client_card.id,
            'category': client_card.category,  # Extracting the value of the enum
            'question': client_card.question,
            'answer': client_card.answer,
            'tags': client_card.tags
        }


def deserialize_user_data(json_data: Dict) -> CardUserData:
      return CardUserData(question=json_data['question'],
        answer=json_data['answer'],
        tag=json_data['tag'])
