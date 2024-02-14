from typing import List
from dataclasses import dataclass


@dataclass
class CardUserData:
    question : str
    answer: str
    tag : str