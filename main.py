from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/images", StaticFiles(directory="images/"))


from routers.auth import auth_roters

app.include_router(auth_roters, tags=["auth"])




# ADD SQLADMIN 
from sqladmin import Admin
from database import engine
from security import AdminAuth
from models.admins_models import (
    UserAdmin,
    UserTokenAdmin,
    UserStatusAdmin,
    CityAdmin,
    ItemAdmin,
    CharacterAdmin,
    TokenAuthAdmin,
    AdminPanelUserAdmin,
)

back_auth = AdminAuth(secret_key="YWRtaW4=")
admin = Admin(app, engine, authentication_backend=back_auth, base_url="/YWRtaW5fcGFuZWwK")

admin.add_view(UserAdmin)
admin.add_view(UserTokenAdmin)
admin.add_view(UserStatusAdmin)
admin.add_view(CityAdmin)
admin.add_view(ItemAdmin)
admin.add_view(CharacterAdmin)
admin.add_view(TokenAuthAdmin)
admin.add_view(AdminPanelUserAdmin)