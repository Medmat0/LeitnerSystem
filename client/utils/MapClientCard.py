from domain.models.Card import Card
from client.dto.ClientCart import ClientCard
from typing import Dict
from domain.models.CardUserData import CardUserData


def map_domain_card_to_client_card (card : Card) -> ClientCard:
   """"
   Fonction pour mapper une carte du domaine vers une carte cliente.

   Args:
       card (Card): La carte du domaine à mapper.

   Returns:
       ClientCard: La carte cliente mappée.
      
   """
   client_card = ClientCard
   client_card.id = card.id
   client_card.answer = card.answer
   client_card.category = card.category
   client_card.question = card.question
   client_card.tags = card.tags
   return client_card


def serialize_client_card(client_card : ClientCard) :
      """
       Fonction pour sérialiser une carte cliente en un dictionnaire JSON.

       Args:
       client_card (ClientCard): La carte cliente à sérialiser.

       Returns:
       dict: Le dictionnaire JSON représentant la carte cliente.
      """
   
      return {
            'id': client_card.id,
            'category': client_card.category,  # Extracting the value of the enum
            'question': client_card.question,
            'answer': client_card.answer,
            'tags': client_card.tags
        }


def deserialize_user_data(json_data: Dict) -> CardUserData:

      """
       Fonction pour désérialiser les données JSON en un objet CardUserData.

        Args:
           json_data (Dict): Les données JSON à désérialiser.

      Returns:
       CardUserData: L'objet CardUserData désérialisé.
      """
      return CardUserData(question=json_data['question'],
        answer=json_data['answer'],
        tag=json_data['tag'])
