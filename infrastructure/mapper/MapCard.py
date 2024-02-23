from infrastructure.entity.CardEntity import CardEntity
from domain.models.Card import Card



def map_card_to_server(card: Card) -> CardEntity:
    return CardEntity(
        id=card.id,
        category=card.category.name,
        question=card.question,
        answer=card.answer,
        tag=card.tags,
        
    )


def map_card_entity_to_domain(card_entity: CardEntity) -> Card:
    return Card(
        id= card_entity.id,
        category=card_entity.category ,
        question=card_entity.question,
        answer=card_entity.answer,
        tags=card_entity.tag,
        nextDateReview =card_entity.date_next_response
    )