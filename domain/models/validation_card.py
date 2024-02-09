
from .user_input import UserInput
from typing import List

def isEmpty(input : str):
        if(input.strip()):
            return False
        else:
            return True

class ValidationCard:
  

    def __init__(self, question: str, answer: str, tags: List[str] = None):
        self.question = question
        self.answer = answer
        self.tags = tags if tags else []
  
    def validate(UserInput): 
        if not isEmpty(UserInput.question) or not isEmpty(UserInput.answer):
            raise ValueError("Toutes les champs doivent être remplis.") 
        else :
             return ValidationCard(
                  question=UserInput.question,
                  answer=UserInput.answer,
                  tags=UserInput.tags
             )
        
    #UserInput Service for notvalid card 
    def isNotValid(user_input : UserInput):
       if  isEmpty(user_input.question):
           return ValueError("Please fill up the question !") , True
       
       if  isEmpty(user_input.answer):
           return ValueError("Please fill up the answer !") , True
       
       if  isEmpty(user_input.answer,user_input.question):
           return ValueError("Must fill up question and answer please !") , True
       
    #UserInput Service for valid card
    def isValid(user_input : UserInput):
       if isEmpty(UserInput.question) or  isEmpty(UserInput.answer):
            return False
       else:
            return True
       
    #CreateValid card service          
    def createValidCard(user_input : UserInput) : 
        return  ValidationCard(
                  question=user_input.question,
                  answer=user_input.answer,
                  tags=user_input.tags
             ) 
    
         
    
        
   

# faut refaire le mecanisme de UserInput -> ValidationCard -> CreateCard -> Card after launching test for creat card !!!!!              
        
        # UserInput = example 
        #  validcard = userinput
        #if(validcard.Isvalid)
        #validcard.createCard this method is for for cards
        #else    validcard.IsNotValid


