from infrastructure.entity.CardEntity import db, CardEntity

class CreateCardServer:
    def save_card(self, card_entity: CardEntity) -> None:
        db.session.add(card_entity)
        db.session.commit()


