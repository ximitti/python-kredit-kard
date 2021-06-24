from app.models.users_model import UsersModel
from faker import Faker
from werkzeug.security import generate_password_hash

# ------------------------------------

fake = Faker("pt_BR")

# -------------------------------------


def create_admin() -> dict:
    login = f"{fake.first_name()} {fake.last_name()}"
    password = fake.password(special_chars=True, upper_case=True, lower_case=True, digits=True)
    password_hash = generate_password_hash(password)

    return {
        "admin": UsersModel(login=login, is_admin=True, password_hash=password_hash),
        "login": login,
        "password": password,
    }
