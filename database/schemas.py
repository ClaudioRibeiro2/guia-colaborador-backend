from datetime import date
from pydantic import BaseModel


class AdministradorModel(BaseModel):
  id_administrador: int
  nome_completo: str
  email: str
  data_nascimento: date
  senha: str
  
  class Config:
    orm_mode: True
class ConteudoModel(BaseModel):
  id_conteudo: int
  titulo: str
  tipo: str
  corpo: str
  id_administrador: int
  
  class Config:
    orm_mode: True
class ColaboradorModel(BaseModel):
  id_colaborador: int
  email: str
  data_nascimento: date
  senha: str
  id_administrador: int
  
  class Config:
    orm_mode = True  