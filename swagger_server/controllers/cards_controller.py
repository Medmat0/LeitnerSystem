import connexion
import six

from swagger_server.models.card import Card  # noqa: E501
from swagger_server.models.card_user_data import CardUserData  # noqa: E501
from swagger_server import util


def cards_get(tags=None):  # noqa: E501
    """Get all cards

    Used to fetch every cards with given tags. If no tags are provided, will fetch all cards. # noqa: E501

    :param tags: Tags of cards to find. If not present, all cards will be found.
    :type tags: List[str]

    :rtype: List[Card]
    """
    return 'do some magic!'


def cards_post(body=None):  # noqa: E501
    """Create a card

    Used to create a new card in the system. A new card will be present in the next quizz. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Card
    """
    if connexion.request.is_json:
        body = CardUserData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
