from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount('/static', StaticFiles(directory='static', html=True), name="static")

@app.get('/')
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Welcome to my Portfolio!"})

