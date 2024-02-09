# application/services/tests/test_card_service.py
import unittest
from unittest.mock import MagicMock, patch

from services.cardServices import CardRepository
from domain.models.cardmodel.user_input import UserInput
from application.services.card_services import CardService

class TestCardService(unittest.TestCase):
    def setUp(self):
        # Créer une implémentation de test du repository (peut être un adaptateur en mémoire)
        self.repository = MagicMock(spec=CardRepository)
        self.service = CardService(card_repository=self.repository)

    def test_create_card(self):
        # Teste la création d'une carte
        userinput = UserInput
        userinput.question = "Test Question"
        userinput.answer = "Test Answer"
        userinput.tags = ["Test"]
        
        card = self.service.create_card(userinput)
        # Assurez-vous que la carte a été ajoutée au repository
        self.repository.add_card.assert_called_once_with(card)

    def test_get_cards(self):
        # Teste la récupération de cartes
        tags = ["Test"]
        self.service.get_cards(tags)
        # Assurez-vous que la méthode get_cards a été appelée avec les tags spécifiques
        self.repository.get_cards.assert_called_once_with(tags)

if __name__ == '__main__':
    unittest.main()
