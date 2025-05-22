from sqlalchemy import Column, Integer, String
from database import Base

class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255))
    tecnologia = Column(String(100))
    link = Column(String(255)) 