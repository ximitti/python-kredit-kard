from flask import current_app
from flask_sqlalchemy import Model

# -----------------------------


def add_commit(model: Model) -> None:
    session = current_app.db.session

    session.add(model)
    session.commit()
