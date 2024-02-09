# domain/tests/test_card_repository.py
import unittest
from unittest.mock import MagicMock
from domain.models.cardmodel.card import Card
from services.cardServices  import CardRepository

class TestCardRepository(unittest.TestCase):
    def setUp(self):
        # Créer une implémentation de test du repository (peut être un adaptateur en mémoire)
        self.repository = MagicMock(spec=CardRepository)

    def test_add_card(self):
        card = Card(question="Test Question", answer="Test Answer", tags=["Test"])
        self.repository.add_card(card)
        # Assurez-vous que la méthode add_card a été appelée avec la carte correcte
        self.repository.add_card.assert_called_once_with(card)

    def test_get_cards_all(self):
        # Teste la récupération de toutes les cartes
        cards = self.repository.get_cards()
        # Assurez-vous que la méthode get_cards a été appelée sans filtre de tags
        self.repository.get_cards.assert_called_once_with()

    def test_get_cards_with_tags(self):
        # Teste la récupération de cartes avec des tags spécifiques
        tags = ["Test"]
        cards = self.repository.get_cards(tags)
        # Assurez-vous que la méthode get_cards a été appelée avec les tags spécifiques
        self.repository.get_cards.assert_called_once_with(tags)

if __name__ == '__main__':
    unittest.main()
