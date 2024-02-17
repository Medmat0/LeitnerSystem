from dataclasses import dataclass
from domain.models.Category import Category


@dataclass
class ClientCard:
    id : str
    category : Category
    question: str
    answer: str
    tags: str 