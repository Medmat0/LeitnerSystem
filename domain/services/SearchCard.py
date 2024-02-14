
from models.Card import Card
from typing import List
from server.repository.SearchCardServer import SearchCardServer
from server.mapper.MapCard import map_card_entity_to_domain

class SearchCardService: 
 
    def __init__(self, searchCardServer: SearchCardServer):
        self.searchCardServer = searchCardServer

    def get_cards_by_tag(self, tag: str) -> List[Card]:
        card_entities = self.searchCardServer.find_by_tag(tag)
        cards = [map_card_entity_to_domain(card_entity) for card_entity in card_entities]
        return cards