from datetime import date
from pydantic import BaseModel


class AdministradorModel(BaseModel):
  nome_completo: str
  email: str
  data_nascimento: date
  senha: str
  
  class Config:
    orm_mode: True
class ConteudoModel(BaseModel):
  titulo: str
  tipo: str
  corpo: str
  id_administrador: int
  
  class Config:
    orm_mode: True
class ColaboradorModel(BaseModel):
  nome_completo:str
  email: str
  data_nascimento: date
  senha: str
  id_administrador: int
  
  class Config:
    orm_mode = True  