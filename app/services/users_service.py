from app.models.users_model import UsersModel
from faker import Faker
from werkzeug.security import generate_password_hash

# ------------------------------------

fake = Faker("pt_BR")

# -------------------------------------


def create_user() -> UsersModel:

    return UsersModel(
        login=f"{fake.first_name()} {fake.last_name()}",
        password_hash=generate_password_hash(
            fake.password(special_chars=True, upper_case=True, lower_case=True, digits=True)
        ),
    )
