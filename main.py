from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/')
def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Welcome to my Portfolio!"})

