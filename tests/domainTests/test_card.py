import unittest
from datetime import datetime, timedelta
from domain.models.cardmodel.card import *



class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("What is the capital of France?", "Paris", ["geography"])

    def test_initialization(self):
        self.assertEqual(self.card.question, "What is the capital of France?")
        self.assertEqual(self.card.answer, "Paris")
        self.assertEqual(self.card.tags, ["geography"])
        self.assertEqual(self.card.category, Category.FIRST)
        self.assertIsNone(self.card.next_review_date)

    def test_update_category_correct_answer(self):
        self.card.category = Category.THIRD
        self.card.update_category(is_correct=True)
        self.assertEqual(self.card.category, Category.FOURTH)  # Category should be incremented

    def test_update_category_incorrect_answer(self):
        self.card.category = Category.FIFTH
        self.card.update_category(is_correct=False)
        self.assertEqual(self.card.category, Category.FIRST)  # Category should reset to 1

    def test_update_next_review_date(self):
        self.card.category = Category.SECOND
        self.card.update_next_review_date()
        expected_date = datetime.now() + timedelta(days=2)
        self.assertEqual(self.card.next_review_date.date(), expected_date.date())

if __name__ == "__main__":
    unittest.main()