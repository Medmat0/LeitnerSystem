""" 



def isEmpty(input : str):
        if(input.strip()):
            return False
        else:
            return True  
    
class UserInputServices:

  


        
    @abstractmethod
    def isNotValid(user_input : UserInput):
       if  isEmpty(user_input.question):
           return ValueError("Please fill up the question !") 
       
       if  isEmpty(user_input.answer):
           return ValueError("Please fill up the answer !") 
       
       if  isEmpty(user_input.answer,user_input.question):
           return ValueError("Must fill up question and answer please !") 
       
    @abstractmethod
    def isValid(user_input : UserInput):
       if isEmpty(UserInput.question) or  isEmpty(UserInput.answer):
            return False
       else:
            return True
       
    @abstractmethod
    def createValidCard(user_input : UserInput) : 
        return  CardServices.add_card(
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


 """