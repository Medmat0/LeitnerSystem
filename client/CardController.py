from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from infrastructure.entity.CardEntity import db

from domain.services.CreateCardService import CreateCardService
from domain.services.AnswerCardService import AnswerCardService
from domain.services.QuizzCardService import QuizzCardService
from domain.services.SearchCardService import SearchCardService

from client.utils.MapClientCard import map_domain_card_to_client_card
from client.utils.MapClientCard import serialize_client_card
from client.utils.MapClientCard import deserialize_user_data


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 


create_card_service = CreateCardService()
answser_card_service = AnswerCardService()
quizz_card_service = QuizzCardService()
search_card_service = SearchCardService()


class Cards(Resource):
    def get(self):
        tags = request.args.getlist('tags')
        if not tags : 
            tags = ''
        cards = search_card_service.get_cards_by_tag(tags)
        client_cards = [map_domain_card_to_client_card(card) for card in cards] 
        client_card_json = [serialize_client_card(client_card) for client_card in client_cards ]
        if client_card_json :
            return jsonify([card  for  card in client_card_json])
        else:
            return  404
        
        
    def post(self):
        card_data = request.get_json()
        card_userdata = deserialize_user_data(card_data)
        card = create_card_service.CreateCard(card_userdata)
        client_card = map_domain_card_to_client_card(card)
        client_card_json = serialize_client_card(client_card)
        if(client_card_json):
             return jsonify(client_card_json)
        else:
            return 404
       
    
api.add_resource(Cards, '/cards')

class Quizz(Resource):
    def get(self):
        quizz_date = request.args.get('date')
        cards = quizz_card_service.fetch_cards_for_quiz(quizz_date)
        client_cards = [map_domain_card_to_client_card(card) for card in cards]
        client_card_json = [serialize_client_card(client_card) for client_card in client_cards ]

        if client_card_json:
            return jsonify([card  for  card in client_card_json])
        else :
            return 404
api.add_resource(Quizz, '/cards/quizz')

class Answer(Resource):
    def patch(self, card_id):
        try:
            card_uuid = str(card_id)
            
        except ValueError:
             return  400
        is_correct = request.json['isValid']
        if answser_card_service.answer_card(card_uuid,is_correct) == 204:
             return 204
        elif answser_card_service.answer_card(card_uuid,is_correct) == 400:
            return 400
        else:
            return 404
    
api.add_resource(Answer, '/cards/<string:card_id>/answer')

if __name__ == '__main__':
    app.run(debug=True)