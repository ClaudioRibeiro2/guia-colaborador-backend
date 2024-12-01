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

class ConteudoResponseModel(BaseModel):
  id_conteudo: int
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
    
class ColaboradorResponseModel(BaseModel):
  id_colaborador: int
  nome_completo:str
  email: str
  data_nascimento: datetime
  senha: str
  id_administrador: int
  
  class Config:
    orm_mode = True  