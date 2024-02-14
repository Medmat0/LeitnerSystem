# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CardUserData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, question: str=None, answer: str=None, tag: str=None):  # noqa: E501
        """CardUserData - a model defined in Swagger

        :param question: The question of this CardUserData.  # noqa: E501
        :type question: str
        :param answer: The answer of this CardUserData.  # noqa: E501
        :type answer: str
        :param tag: The tag of this CardUserData.  # noqa: E501
        :type tag: str
        """
        self.swagger_types = {
            'question': str,
            'answer': str,
            'tag': str
        }

        self.attribute_map = {
            'question': 'question',
            'answer': 'answer',
            'tag': 'tag'
        }
        self._question = question
        self._answer = answer
        self._tag = tag

    @classmethod
    def from_dict(cls, dikt) -> 'CardUserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardUserData of this CardUserData.  # noqa: E501
        :rtype: CardUserData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def question(self) -> str:
        """Gets the question of this CardUserData.

        Question to be asked to the user during a quizz  # noqa: E501

        :return: The question of this CardUserData.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question: str):
        """Sets the question of this CardUserData.

        Question to be asked to the user during a quizz  # noqa: E501

        :param question: The question of this CardUserData.
        :type question: str
        """
        if question is None:
            raise ValueError("Invalid value for `question`, must not be `None`")  # noqa: E501

        self._question = question

    @property
    def answer(self) -> str:
        """Gets the answer of this CardUserData.

        Expected answer for the question  # noqa: E501

        :return: The answer of this CardUserData.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Sets the answer of this CardUserData.

        Expected answer for the question  # noqa: E501

        :param answer: The answer of this CardUserData.
        :type answer: str
        """
        if answer is None:
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer

    @property
    def tag(self) -> str:
        """Gets the tag of this CardUserData.

        A tag to group cards on same topic  # noqa: E501

        :return: The tag of this CardUserData.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag: str):
        """Sets the tag of this CardUserData.

        A tag to group cards on same topic  # noqa: E501

        :param tag: The tag of this CardUserData.
        :type tag: str
        """

        self._tag = tag