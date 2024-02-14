import connexion
import six

from swagger_server.models.card import Card  # noqa: E501
from swagger_server.models.card_id import CardId  # noqa: E501
from swagger_server.models.card_id_answer_body import CardIdAnswerBody  # noqa: E501
from swagger_server import util


def cards_card_id_answer_patch(card_id, body=None):  # noqa: E501
    """Answer a question

    Used to answer a question. Body indicate if user has answered correctly or not. # noqa: E501

    :param card_id: Id of answered card.
    :type card_id: dict | bytes
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        card_id = CardId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = CardIdAnswerBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cards_quizz_get(_date=None):  # noqa: E501
    """Cards for the day

    Used to fetch all cards for a quizz at a given date. If no date is provided, quizz will be for today. # noqa: E501

    :param _date: Date of quizz. If not provided, date will be today.
    :type _date: str

    :rtype: List[Card]
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'
