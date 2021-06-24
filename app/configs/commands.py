from flask import Flask, current_app
from flask.cli import AppGroup
from click import echo, argument
from faker import Faker
from werkzeug.security import generate_password_hash
import random

from app.models.users_model import UsersModel
from app.models.credit_cards_model import CreditCardsModel


# ------------------------------------

fake = Faker("pt_BR")

# ------------------------------------


def cli_user(app: Flask):
    cli_user_group = AppGroup("user")

    @cli_user_group.command("create")
    @argument("quantity")
    def cli_user_create(quantity: int):
        session = current_app.db.session

        for _ in range(int(quantity)):
            login = f"{fake.first_name()} {fake.last_name()}"
            password_hash = generate_password_hash(
                fake.password(special_chars=True, upper_case=True, lower_case=True, digits=True)
            )

            new_user: UsersModel = UsersModel(login=login, password_hash=password_hash)

            session.add(new_user)
            session.commit()

    app.cli.add_command(cli_user_group)


def cli_admin(app: Flask):
    cli_admin_group = AppGroup("admin")

    @cli_admin_group.command("create")
    def cli_admin_create():
        session = current_app.db.session

        login = f"{fake.first_name()} {fake.last_name()}"
        password = fake.password(special_chars=True, upper_case=True, lower_case=True, digits=True)
        password_hash = generate_password_hash(password)

        new_user: UsersModel = UsersModel(login=login, is_admin=True, password_hash=password_hash)

        session.add(new_user)
        session.commit()

        echo("Admin criado!!")
        echo(f"login: {login}")
        echo(f"password: {password}")

    app.cli.add_command(cli_admin_group)


def cli_users_credit_cards(app: Flask):
    cli_users_credit_cards_group = AppGroup("users_credit_cards")

    @cli_users_credit_cards_group.command("create")
    @argument("quantity")
    def cli_users_credit_cards_create(quantity: int):
        session = current_app.db.session

        for _ in range(int(quantity)):
            login = f"{fake.first_name()} {fake.last_name()}"
            password_hash = generate_password_hash(
                fake.password(special_chars=True, upper_case=True, lower_case=True, digits=True)
            )

            new_user: UsersModel = UsersModel(login=login, password_hash=password_hash)

            session.add(new_user)
            session.commit()

            credit_cards = random.randrange(0, 3)

            if credit_cards > 0:
                for _ in range(int(credit_cards)):
                    expire_date = fake.credit_card_expire()
                    number = fake.credit_card_number()
                    provider = fake.credit_card_provider()
                    security_code = fake.credit_card_security_code(card_type="visa")
                    user_id = new_user.id

                    new_credit_card = CreditCardsModel(
                        expire_date=expire_date,
                        number=number,
                        provider=provider,
                        security_code=security_code,
                        user_id=user_id,
                    )

                    session.add(new_credit_card)
                    session.commit()

    app.cli.add_command(cli_users_credit_cards_group)


def init_app(app: Flask):
    cli_user(app)
    cli_admin(app)
    cli_users_credit_cards(app)
