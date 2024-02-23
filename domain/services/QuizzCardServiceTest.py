import unittest
from datetime import datetime
from QuizzCardService import QuizzCardService

class TestQuizzCardService(unittest.TestCase):
    
    def setUp(self):
        self.quizz_card_service = QuizzCardService()
        
    def test_fetch_cards_for_quiz_no_cards(self):
     
        mock_quiz_date = datetime(2024, 2, 11)
        
       
        cards = self.quizz_card_service.fetch_cards_for_quiz(mock_quiz_date)
        
      
        self.assertEqual(len(cards), 0)
        
    

if __name__ == '__main__':
    unittest.main()
