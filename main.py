from dataclasses import dataclass
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi import Form
from pathlib import Path
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
    imagem: str  # <- Recolocado aqui

# Lista de projetos
projetos = [
    Projeto(
        id=1,
        nome="Chatbot FURIA",
        descricao="Um chatbot desenvolvido para os fãs do time de CS:GO da FURIA",
        tecnologias=["Python", "FastAPI", "HTML", "CSS"],
        status="Concluído",
        categoria="Fullstack",
        link="https://furia-bot-pi.vercel.app",
        imagem="static/img/chatbot_furia.jpg"
       ),
    Projeto(
        id=2,
        nome="Zarro Catálogo",
        descricao="Site para loja de cerâmica artesanal.",
        tecnologias=["Python", "HTML", "CSS"],
        status="Em desenvolvimento",
        categoria="Web",
        link="https://github.com/aclfilho/zarro",
        imagem="/static/img/zarro.png"  
    ),
    
    Projeto(
    id=3,
    nome="Biblioteca Pessoal",
    descricao="Sistema web para registrar e organizar livros lidos, com avaliações, filtros e estatísticas.",
    tecnologias=["Python", "FastAPI", "React", "JSON"],
    status="Em desenvolvimento",
    categoria="Fullstack",
    link="https://github.com/aclfilho/biblioteca-pessoal",
    imagem="/static/img/biblioteca.png"
),
]


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "projetos": projetos})

@app.get("/contato")
def contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.get("/projetos")
def pagina_projetos(request: Request):
    return templates.TemplateResponse("projetos.html", {"request": request, "projetos": projetos})

