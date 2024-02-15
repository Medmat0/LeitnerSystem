from datetime import datetime
from typing import List
from entity.CardEntity import CardEntity


class QuizzCardServer:
    
    
     def findQuizzCardDay(self,date: datetime) -> List[CardEntity]:
        
       
        cardEntities =   CardEntity.query.filter_by(date_next_response = date).all()
        
        
        return cardEntities

        