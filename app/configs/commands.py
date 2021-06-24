from flask import Flask
from flask.cli import AppGroup
from click import echo, argument
import random

from app.services import add_commit, create_admin, create_user, create_credit_card


# ------------------------------------


def cli_user(app: Flask):
    cli_user_group = AppGroup("user")

    @cli_user_group.command("create")
    @argument("quantity")
    def cli_user_create(quantity: int):

        for _ in range(int(quantity)):
            new_user = create_user()
            add_commit(new_user)

    app.cli.add_command(cli_user_group)


def cli_admin(app: Flask):
    cli_admin_group = AppGroup("admin")

    @cli_admin_group.command("create")
    def cli_admin_create():

        new_admin = create_admin()
        add_commit(new_admin.get("admin"))

        echo("Admin criado!!")
        echo(f"login: {new_admin.get('login')}")
        echo(f"password: {new_admin.get('password')}")

    app.cli.add_command(cli_admin_group)


def cli_users_credit_cards(app: Flask):
    cli_users_credit_cards_group = AppGroup("users_credit_cards")

    @cli_users_credit_cards_group.command("create")
    @argument("quantity")
    def cli_users_credit_cards_create(quantity: int):

        for _ in range(int(quantity)):
            new_user = create_user()
            add_commit(new_user)

            for _ in range(int(random.randrange(0, 3))):
                new_credit_card = create_credit_card(new_user)
                add_commit(new_credit_card)

    app.cli.add_command(cli_users_credit_cards_group)


def init_app(app: Flask):
    cli_user(app)
    cli_admin(app)
    cli_users_credit_cards(app)
