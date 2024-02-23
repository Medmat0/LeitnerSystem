import unittest
from domain.services.CreateCardService import CreateCardService
from domain.models.CardUserData import CardUserData

class TestCreateCardService(unittest.TestCase):

    def setUp(self):
        self.createCardService = CreateCardService()

    def test_CreateCard_valid_input(self):
        card_userdata = CardUserData("Question", "Answer", "Tag")
        card = self.createCardService.CreateCard(card_userdata)
        self.assertIsNotNone(card)

    def test_CreateCard_empty_question(self):
        card_userdata = CardUserData("", "Answer", "Tag")
        with self.assertRaises(ValueError):
            self.createCardService.CreateCard(card_userdata)

    def test_CreateCard_empty_answer(self):
        card_userdata = CardUserData("Question", "", "Tag")
        with self.assertRaises(ValueError):
            self.createCardService.CreateCard(card_userdata)

if __name__ == '__main__':
    unittest.main()
