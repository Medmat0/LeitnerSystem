# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.card import Card  # noqa: E501
from swagger_server.models.card_user_data import CardUserData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCardsController(BaseTestCase):
    """CardsController integration test stubs"""

    def test_cards_get(self):
        """Test case for cards_get

        Get all cards
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open(
            '/cards',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cards_post(self):
        """Test case for cards_post

        Create a card
        """
        body = CardUserData()
        response = self.client.open(
            '/cards',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
