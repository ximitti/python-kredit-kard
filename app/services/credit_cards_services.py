from flask_sqlalchemy import Model
from faker import Faker

from app.models.credit_cards_model import CreditCardsModel

# ----------------------------------

fake = Faker("pt_BR")

# ----------------------------------


def create_credit_card(user: Model) -> CreditCardsModel:

    return CreditCardsModel(
        expire_date=fake.credit_card_expire(),
        number=fake.credit_card_number(),
        provider=fake.credit_card_provider(),
        security_code=fake.credit_card_security_code(card_type="visa"),
        user_id=user.id,
    )
