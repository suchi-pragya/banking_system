# import fastapi and create root path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
