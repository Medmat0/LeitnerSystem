
from domain.models.Card import Card
from typing import List
from infrastructure.repository.SearchCardServer import SearchCardServer
from infrastructure.mapper.MapCard import map_card_entity_to_domain

class SearchCardService: 
 
    def __init__(self, searchCardServer: SearchCardServer):
        self.searchCardServer = searchCardServer

    def get_cards_by_tag(self, tags: List[str] ) -> List[Card]:
        cards = []      
        #if tags:
        for tag in tags:
                card_entities = self.searchCardServer.findByTag(tag)
                
        #else:
            #card_entities = self.searchCardServer.getAllCard()
        cards = [map_card_entity_to_domain(card_entity) for card_entity in card_entities]
        return cards 