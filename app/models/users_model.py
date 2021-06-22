from . import db
from sqlalchemy import Column, Integer, String, Boolean
from dataclasses import dataclass


# ----------------------------------


@dataclass
class UsersModel(db.Model):
    login: str
    password_hash: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    login = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    password_hash = Column(String, nullable=True)
