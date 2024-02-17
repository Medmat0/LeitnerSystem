from typing import  Optional
from datetime import datetime
from dataclasses import dataclass
from domain.models.CardId import CardId
from domain.models.Category import Category


@dataclass
class Card:
   id: CardId
   category : Category
   question: str
   answer: str
   tags: str 
   nextDateReview : Optional[datetime] = datetime.now()
