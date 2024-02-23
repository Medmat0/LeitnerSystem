import unittest
from MapCard import map_card_to_server, map_card_entity_to_domain
from infrastructure.entity.CardEntity import CardEntity
from domain.models.Card import Card, Category

class TestCardMapping(unittest.TestCase):
    
    def setUp(self):
        self.card = Card(id="123", category=Category.FIRST, question="Question", answer="Answer", tags=["tag1", "tag2"])
        
        self.card_entity = CardEntity(id="123", category="FIRST", question="Question", answer="Answer", tag=["tag1", "tag2"])
        
    def test_map_card_to_server(self):
        mapped_card_entity = map_card_to_server(self.card)
        
        self.assertEqual(mapped_card_entity.id, self.card_entity.id)
        self.assertEqual(mapped_card_entity.category, self.card_entity.category)
        self.assertEqual(mapped_card_entity.question, self.card_entity.question)
        self.assertEqual(mapped_card_entity.answer, self.card_entity.answer)
        self.assertEqual(mapped_card_entity.tag, self.card_entity.tag)
        
    def test_map_card_entity_to_domain(self):
        mapped_card = map_card_entity_to_domain(self.card_entity)
        
        self.assertEqual(mapped_card.id, self.card_entity.id)
        self.assertEqual(mapped_card.category, self.card_entity.category)
        self.assertEqual(mapped_card.question, self.card_entity.question)
        self.assertEqual(mapped_card.answer, self.card_entity.answer)
        self.assertEqual(mapped_card.tags, self.card_entity.tag)

if __name__ == '__main__':
    unittest.main()
