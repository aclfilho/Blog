from fastapi import FastAPI, Request
from fastapi import Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from database import SessionLocal
from models import Projeto, Base
from sqlalchemy.orm import Session
from sqlalchemy import select

app = FastAPI()

# cria tabelas (caso ainda não existam)
Base.metadata.create_all(bind=SessionLocal().get_bind())

# Configurações de caminho
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Dependência para obter uma sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# configuração para caminho dos templates e arq estáticos
BASE_DIR = Path(__file__).resolve().parent #pega o caminho da pasta atual
templates = Jinja2Templates(directory=str(BASE_DIR / "templates")) #diz ao FastAPI onde estão os html
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static") #permite servir os arquivos estáticos que ficam em static


#p ágina inicial usando dados reais do banco
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    projetos = db.execute(select(Projeto)).scalars().all()
    return templates.TemplateResponse("index.html", {"request": request, "projetos": projetos})


@app.get("/sobre")
def sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})


@app.get("/contato")
def contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})
