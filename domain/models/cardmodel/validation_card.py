
from user_input import UserInput
from typing import List

def isNotEmpty(input : str):
        if(input.strip()):
            return True
        else:
            return False

class ValidationCard(UserInput):

    def __init__(self, question: str, answer: str, tags: List[str] = None):
        super().__init__(question, answer, tags)

    def validate(self):
        if not self.isNotEmpty(self.question) or not self.isNotEmpty(self.answer):
            raise ValueError("Toutes les champs doivent être remplis.") 
        

    
        
   

