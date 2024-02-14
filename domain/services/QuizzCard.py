from datetime import datetime, timedelta
from models.Card import Card
from typing import List

def getQuizDay(day: str = None) -> datetime:
    if day:
        quiz_date = datetime.strptime(day, '%Y-%m-%d')
    else:
        quiz_date = datetime.now().date()
    return quiz_date

def fetch_cards_for_quiz(quiz_date: datetime) -> List[Card]:
    pass