from sqladmin import ModelView
from .models import (
    User,
    UserToken,
    UserStatus,
    City,
    Item,
    Character,
    TokenAuth,
    AdminPanelUser
)

class UserAdmin(ModelView, model=User):
    column_list = "__all__"

class UserTokenAdmin(ModelView, model=UserToken):
    column_list = "__all__"

class UserStatusAdmin(ModelView, model=UserStatus):
    column_list = "__all__"

class CityAdmin(ModelView, model=City):
    column_list = "__all__"

class ItemAdmin(ModelView, model=Item):
    column_list = "__all__"

class CharacterAdmin(ModelView, model=Character):
    column_list = "__all__"

class TokenAuthAdmin(ModelView, model=TokenAuth):
    column_list = "__all__"

class AdminPanelUserAdmin(ModelView, model=AdminPanelUser):
    column_list = "__all__"
