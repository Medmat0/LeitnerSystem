import unittest
from SearchCardService import SearchCardService

class TestSearchCardService(unittest.TestCase):
    
    def setUp(self):
        self.search_card_service = SearchCardService()
        
    def test_get_cards_by_tag_with_tags(self):
        mock_tags = ["tag1", "tag2", "tag3"]
       
        cards = self.search_card_service.get_cards_by_tag(mock_tags)
        
        self.assertIsInstance(cards, list)
        
       
    
    def test_get_cards_by_tag_no_tags(self):

        mock_tags = []
        

        cards = self.search_card_service.get_cards_by_tag(mock_tags)
        

        self.assertIsInstance(cards, list)
        
  
    

if __name__ == '__main__':
    unittest.main()
