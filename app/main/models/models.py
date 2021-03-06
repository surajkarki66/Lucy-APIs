from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Enum

from ..infrastructure.database.db import Base
from ..schemas.schemas import Role


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default="subscriber")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, nullable=False)
    person_name = Column(String(255), nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)