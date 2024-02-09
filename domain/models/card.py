from typing import List, Optional
from enum import Enum
from datetime import datetime, timedelta

class Category(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    DONE = 10   


class Card:
    def __init__(self, question: str, answer: str, tags: List[str] = None):
        self.question = question
        self.answer = answer
        self.tags = tags if tags else []
        self.category = Category.FIRST
        self.next_review_date: Optional[datetime] = None

    def update_category(self, is_correct: bool):
        if is_correct:
            if self.category.value < Category.SEVENTH.value:  # Compare enum values
                self.category = Category(self.category.value + 1)
            else:
                self.category = Category.LEARNED
        else:
            self.category = Category.FIRST  # Incorrect answer, reset to the first category
        self.update_next_review_date()

    def update_next_review_date(self):
        days_to_next_review = 2 ** (self.category.value - 1)  # Calcul de la prochaine révision
        self.next_review_date = datetime.now() + timedelta(days=days_to_next_review)



        # in enum <> doenst WORK should impl it in ENUM 
