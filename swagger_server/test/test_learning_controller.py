# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.card import Card  # noqa: E501
from swagger_server.models.card_id import CardId  # noqa: E501
from swagger_server.models.card_id_answer_body import CardIdAnswerBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLearningController(BaseTestCase):
    """LearningController integration test stubs"""

    def test_cards_card_id_answer_patch(self):
        """Test case for cards_card_id_answer_patch

        Answer a question
        """
        body = CardIdAnswerBody()
        response = self.client.open(
            '/cards/{cardId}/answer'.format(card_id=CardId()),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cards_quizz_get(self):
        """Test case for cards_quizz_get

        Cards for the day
        """
        query_string = [('_date', '2013-10-20')]
        response = self.client.open(
            '/cards/quizz',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
