import string
import random


def id_generator():
    character_set = string.ascii_lowercase + string.digits
    remaining = "".join(random.choice(character_set) for _ in range(32))
    return remaining


def user_id_generator():
    character_set = string.ascii_lowercase + string.digits
    remaining = "user_" + "".join(random.choice(character_set) for _ in range(32))
    return remaining


def item_id_generator():
    character_set = string.ascii_lowercase + string.digits
    remaining = "item_" + "".join(random.choice(character_set) for _ in range(32))
    return remaining


def character_id_generator():
    character_set = string.ascii_lowercase + string.digits
    remaining = "character_" + "".join(random.choice(character_set) for _ in range(32))
    return remaining
