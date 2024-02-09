from typing import List

class UserInput():

    def __init__(self, question: str, answer : str ,tags: List[str] = None):
        self.question = question
        self.answer = answer
        self.tags = tags if tags else []

        pass