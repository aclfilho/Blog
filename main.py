from dataclasses import dataclass
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from dataclasses import dataclass, field
from typing import List

app = FastAPI()

# Configurações de caminho
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@dataclass
class Projeto:
    id: int
    nome: str
    descricao: str
    link: str
    tecnologias: List[str]
    status: str         
    categoria: str      

# Lista de projetos como objetos Projeto
# Projetos definidos manualmente com os campos certos
projetos = [
    Projeto(
        id=1,
        nome="Chatbot FURIA",
        descricao="Um chatbot desenvolvido para os fãs do time de CS:GO da FURIA",
        tecnologias=["Python", "FastAPI", "HTML", "CSS"],
        status="Concluído",
        categoria="Fullstack",
        link="https://furia-bot-pi.vercel.app"
    ),
    Projeto(
        id=2,
        nome="Treinos",
        descricao="Interface dinâmica para inserir e armazenar meus treinos de forma organizada e que eu possa analisá-los.",
        tecnologias=["Python", "MySQL"],
        status="Concluído",
        categoria="Backend",
        link="https://github.com/aclfilho/First-project"
    ),
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "projetos": projetos})

@app.get("/sobre")
def sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})

@app.get("/contato")
def contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.get("/projetos")
def pagina_projetos(request: Request):
    return templates.TemplateResponse("projetos.html", {"request": request, "projetos": projetos})