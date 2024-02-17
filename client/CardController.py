from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from domain.services.CreateCardService import CreateCardService
from domain.services.AnswerCardService import AnswerCardService
from domain.services.QuizzCardService import QuizzCardService
from domain.services.SearchCardService import SearchCardService
from MapClientCard import map_domain_card_to_client_card
from uuid import UUID
app = Flask(__name__)
api = Api(app)

createCardService = CreateCardService
answserCardService = AnswerCardService
quizzCardService = QuizzCardService
searchCardService = SearchCardService


class Cards(Resource):
    def get(self):
        tags = request.args.getlist('tags')
        if not tags : 
            tags = ''
        cards = searchCardService.get_cards_by_tag(tags)
        clientCard = [map_domain_card_to_client_card(card) for card in cards] 
        if clientCard :
            return  jsonify([card.__dict__ for  card in clientCard])
        else:
            return "NOT FOUND"
    def post(self):
        cardData = request.get_json()
        card = createCardService.CreateCard(cardData)
        clientCard = map_domain_card_to_client_card(card)
        return jsonify(clientCard.__dict__), 201
    
api.add_resource(Cards, '/cards')

class Quizz(Resource):
    def get(self):
        quizzDate = request.get_json('date')
        quizzDate = quizzCardService.getQuizDay(quizzDate)
        cards = quizzCardService.fetch_cards_for_quiz(quizzDate)
        clientCard = map_domain_card_to_client_card(cards)
        return jsonify(card.__dict__ for card in clientCard)
    
api.add_resource(Quizz, '/cards/quizz')

class Answer(Resource):
    def patch(self, cardId):
        try:
            cardUuid = UUID(cardId)
        except ValueError:
             return "Invalid card ID", 400
        isCorrect = request.json['isValid']
        answserCardService.answer_card(cardUuid,isCorrect)
        return '',204
    
api.add_resource(Answer, '/cards/<string:card_id>/answer')

if __name__ == '__main__':
    app.run(debug=True)