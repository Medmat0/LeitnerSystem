from domain.models.Card import Card
from domain.models.Category import Category
from infrastructure.repository.AnswerCardServer import AnswerCardServer


class AnswerCardService:

    def __init__(self) -> None:
        self.answerCardServer = AnswerCardServer()

    def correctAnswer(self, category):
        """
        Détermine la catégorie suivante si la réponse est correcte.

        Args:
            category (str): La catégorie actuelle de la carte.

        Returns:
            str: La catégorie suivante si elle existe, sinon None.
        """

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
        

          
    def wrongAnswer(self):
        """
        Définit la catégorie comme la première en cas de réponse incorrecte.

        Args:
            category (str): La catégorie actuelle de la carte.

        Returns:
            str: La catégorie "FIRST".
        """
        
        return "FIRST"
    
    def answer_card(self, card_id: str, is_correct: bool):
         
        """
        Traite la réponse donnée à une carte.

        Args:
            card_id (str): L'identifiant de la carte.
            is_correct (bool): Indique si la réponse est correcte.

        Returns:
            int: Le code de statut HTTP indiquant le résultat de l'opération.
        """
        card_entity = self.answerCardServer.getCardById(card_id)
        if not card_entity:
            return 404
        
        if is_correct:
            card_entity.category = self.correctAnswer(card_entity.category)
            self.answerCardServer.updateCard(card_entity)
            return 204

         
        else:
            card_entity.category = self.wrongAnswer()   
            self.answerCardServer.updateCard(card_entity)
            return 400
            
       
    

