from entity.CardEntity import CardEntity
from typing import List



class SearchCardServer: 

    def findByTag(self, tag: str = None) -> List[CardEntity]:
        if tag:
            card_entities = CardEntity.query.filter_by(tag=tag).all()
        else:
            card_entities = CardEntity.query.all()

        if not card_entities and not tag:
            card_entities = CardEntity.query.all()

        return card_entities