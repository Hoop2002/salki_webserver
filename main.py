from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/images", StaticFiles(directory="images/"))


from routers.auth import sign_up_roters

app.include_router(sign_up_roters, tags=["auth"])
