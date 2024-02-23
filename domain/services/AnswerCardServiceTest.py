import unittest
from unittest.mock import MagicMock
from domain.models.Card import Card
from infrastructure.repository.AnswerCardServer import AnswerCardServer
from domain.services.AnswerCardService import AnswerCardService


class TestAnswerCardService(unittest.TestCase):

    def setUp(self):
        self.answerCardServer = MagicMock(spec=AnswerCardServer)
        self.answerCardService = AnswerCardService()
        self.answerCardService.answerCardServer = self.answerCardServer

    def test_correct_answer(self):
    
        self.assertEqual(self.answerCardService.correctAnswer("FIRST"), "SECOND")
        self.assertEqual(self.answerCardService.correctAnswer("SECOND"), "THIRD")
        self.assertEqual(self.answerCardService.correctAnswer("THIRD"), "FOURTH")
        self.assertEqual(self.answerCardService.correctAnswer("FOURTH"), "FIFTH")
        self.assertEqual(self.answerCardService.correctAnswer("FIFTH"), "SIXTH")
        self.assertEqual(self.answerCardService.correctAnswer("SIXTH"), "SEVENTH")
        self.assertEqual(self.answerCardService.correctAnswer("SEVENTH"), "DONE")
      
        self.assertIsNone(self.answerCardService.correctAnswer("UNKNOWN"))

    def test_wrong_answer(self):
      
        self.assertEqual(self.answerCardService.wrongAnswer("ANY_CATEGORY"), "FIRST")

    def test_answer_card_correct(self):
       
        card_entity_mock = MagicMock()
        card_entity_mock.category = "FIRST"

        self.answerCardServer.getCardById.return_value = card_entity_mock
        self.answerCardServer.updateCard.return_value = None

      
        response_code = self.answerCardService.answer_card("dummy_card_id", is_correct=True)
        self.assertEqual(response_code, 204)
        self.assertEqual(card_entity_mock.category, "SECOND")

    def test_answer_card_wrong(self):
        
        card_entity_mock = MagicMock()
        card_entity_mock.category = "SECOND"
    
        self.answerCardServer.getCardById.return_value = card_entity_mock
        self.answerCardServer.updateCard.return_value = None

       
        response_code = self.answerCardService.answer_card("dummy_card_id", is_correct=False)
        self.assertEqual(response_code, 400)
        self.assertEqual(card_entity_mock.category, "FIRST")

    def test_answer_card_not_found(self):
    
        self.answerCardServer.getCardById.return_value = None

       
        response_code = self.answerCardService.answer_card("unknown_card_id", is_correct=True)
        self.assertEqual(response_code, 404)


if __name__ == '__main__':
    unittest.main()