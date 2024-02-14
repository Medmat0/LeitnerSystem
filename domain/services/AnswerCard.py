from models.Card import Card
from models.Category import Category


class AnswerCard:

    def correctAnswer( this ,card: Card) -> Card:
        if card.category == Category.SEVENTH:
              card.category = Category.DONE

        elif card.category != Category.SEVENTH:
           card.category = Category(card.category.value + 1)

        return card

    def wrongAnswer( this , card: Card) -> Card:
        card.category = Category.FIRST
        return card
    
    def answer_card(this, card: Card, is_correct: bool) -> Card:
        if is_correct:
            card = this.correctAnswer(card)
        else:
            card = this.wrongAnswer(card)
        return card
    
