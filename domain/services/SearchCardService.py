
from domain.models.Card import Card
from typing import List
from infrastructure.repository.SearchCardServer import SearchCardServer
from infrastructure.mapper.MapCard import map_card_entity_to_domain
from infrastructure.entity.CardEntity import db
from flask import Flask



class SearchCardService: 
    def get_cards_by_tag(self, tags: List[str] ) -> List[Card]:
      
        search_card_server = SearchCardServer()
        cards = []      
        if tags:
                for tag in tags:
                    card_entities = search_card_server.findByTag(tag)
                
        else:
                    card_entities = search_card_server.getAllCard()
                   
        cards = [map_card_entity_to_domain(card_entity) for card_entity in card_entities]
        return cards 
    
