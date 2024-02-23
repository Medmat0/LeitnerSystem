import unittest
from MapClientCard import map_domain_card_to_client_card, serialize_client_card, deserialize_user_data
from client.dto.ClientCart import ClientCard
from domain.models.Card import Card


class TestCardFunctions(unittest.TestCase):
    
    def setUp(self):
        
        self.card = Card(id="123", category="FIRST", question="Question", answer="Answer", tags=["tag1", "tag2"])
    
        self.client_card = ClientCard(id="123", category="FIRST", question="Question", answer="Answer", tags=["tag1", "tag2"])
        
        self.json_data = {'question': 'Question', 'answer': 'Answer', 'tag': 'tag1'}
        
    def test_map_domain_card_to_client_card(self):
     
        mapped_client_card = map_domain_card_to_client_card(self.card)
        
        self.assertEqual(mapped_client_card.id, self.client_card.id)
        self.assertEqual(mapped_client_card.category, self.client_card.category)
        self.assertEqual(mapped_client_card.question, self.client_card.question)
        self.assertEqual(mapped_client_card.answer, self.client_card.answer)
        self.assertEqual(mapped_client_card.tags, self.client_card.tags)
        
    def test_serialize_client_card(self):
      
        serialized_card = serialize_client_card(self.client_card)
        
      
        self.assertEqual(serialized_card['id'], self.client_card.id)
        self.assertEqual(serialized_card['category'], self.client_card.category)
        self.assertEqual(serialized_card['question'], self.client_card.question)
        self.assertEqual(serialized_card['answer'], self.client_card.answer)
        self.assertEqual(serialized_card['tags'], self.client_card.tags)
        
    def test_deserialize_user_data(self):
      
        deserialized_user_data = deserialize_user_data(self.json_data)
        
        self.assertEqual(deserialized_user_data.question, "Question")
        self.assertEqual(deserialized_user_data.answer, "Answer")
        self.assertEqual(deserialized_user_data.tag, "tag1")

if __name__ == '__main__':
    unittest.main()
