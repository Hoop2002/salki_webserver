from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/")
def test(req: Request):
    return {}
