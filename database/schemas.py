from datetime import datetime
from pydantic import BaseModel

class AdministradorModel(BaseModel):
  nome_completo: str
  email: str
  data_nascimento: datetime
  senha: str
  
  class Config:
    orm_mode: True

class AdministradorResponseModel(BaseModel):
  id_administrador: int
  nome_completo: str
  email: str
  data_nascimento: datetime
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
  data_nascimento: datetime
  senha: str
  id_administrador: int
  
  class Config:
    orm_mode = True  