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
from sqlalchemy.orm import relationship
from database import Base
from utils import user_id_generator, item_id_generator, character_id_generator
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64), unique=True, default=user_id_generator)
    username = Column(String(128), unique=True)
    email = Column(String(64), unique=True)
    password_hash = Column(String(2048))
    locale = Column(String(2), default="ru")
    verified = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    image_path = Column(String(64), default="images/users/default_icon_user.png")
    balance_coins = Column(Integer, default=0)
    balance_crystals = Column(Integer, default=0)
    create_date = Column(DateTime, default=datetime.utcnow)


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
