from sqlalchemy.orm import relationship
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    DECIMAL,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
)
from database import Base
from utils import user_id_generator, item_id_generator, character_id_generator
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64), unique=True, default=user_id_generator)
    username = Column(String(128), unique=True)
    phone = Column(String(16))
    email = Column(String(64), unique=True)
    password_hash = Column(String(2048))
    locale = Column(String(2), default="ru")
    latitude = Column(DECIMAL, default=0.0)
    longitude = Column(DECIMAL, default=0.0)
    verified = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    image_path = Column(String(64), default="images/users/default_icon_user.png")
    balance_coins = Column(Integer, default=0)
    balance_crystals = Column(Integer, default=0)
    tokens = relationship("UserToken", back_populates="user")
    create_date = Column(DateTime, default=datetime.utcnow)


class UserToken(Base):
    __tablename__ = "users_tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64), ForeignKey("users.user_id"))
    token = Column(String(512), unique=True)
    date_created = Column(DateTime, default=datetime.utcnow)
    date_expired = Column(DateTime)
    user = relationship("User", back_populates="tokens")


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    ext_id = Column(String(32), unique=True)


class UserStatus(Base):
    __tablename__ = "user_status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    ext_id = Column(String(32), unique=True)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(String(64), unique=True, default=item_id_generator)
    name = Column(String(128), unique=True)
    description = Column(Text, unique=False)
    image_path = Column(String(64), default="images/items/default_icon_item.png")
    cost_coins = Column(Integer)
    cost_crystals = Column(Integer)


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    character_id = Column(String(64), unique=True, default=character_id_generator)
    name = Column(String(128), unique=True)
    description = Column(Text, unique=False)
    image_path = Column(
        String(64), default="images/characters/default_icon_character.png"
    )
    cost_coins = Column(Integer)
    cost_crystals = Column(Integer)


class TokenAuth(Base):
    __tablename__ = "tokens_auth"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(512), unique=True)


class AdminPanelUser(Base):
    __tablename__ = "admin_panel_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(64), unique=True)
    password = Column(String(128))
    token = Column(String(512), unique=True)
