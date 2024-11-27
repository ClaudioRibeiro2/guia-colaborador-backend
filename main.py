from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from database import models, schemas
from db import  engine, get_db
from sqlalchemy.orm import Session
from database.repositories import *
import time

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detalhe: {err}"})

@app.middleware("http")
async def add_process_time_header(request, call_next):
    print('dentro no middleware!')
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    return response

# CRUD DE ADMINISTRADOR
@app.post('/administrador', tags=["Administrador"], response_model=schemas.AdministradorModel, status_code=201)
async def create_administrador(administrador_request:schemas.AdministradorModel, db: Session = Depends(get_db)):
  return await AdministradorRepo.create(db=db, administrador=administrador_request)

@app.get('/administrador/{id_administrador}', tags=["Administrador"], response_model=schemas.AdministradorModel)
def get_administrador(id_administrador: int, db: Session = Depends(get_db)):
  db_administrador = AdministradorRepo.read_by_id(db, id_administrador)
  if db_administrador is None:
    raise HTTPException(status_code=404, detail="Administrador não consta em nossa banco de dados :c")
  return db_administrador    

@app.delete('/administrador/{id_administrador}', tags=["Administrador"])
async def delete_administrador(id_administrador: int, db: Session = Depends(get_db)):
  db_administrador = AdministradorRepo.read_by_id(db, id_administrador)
  if db_administrador is None:
    raise HTTPException(status_code=404, detail="Administrador não consta em nossa banco de dados :c")
  await AdministradorRepo.delete(db, id_administrador)
  return "Administrador removido com sucesso!"

@app.put('/administrador/{id_administrador}', tags=["Administrador"], response_model=schemas.AdministradorModel)
async def update_administrador(id_administrador: int, administrador_request: schemas.AdministradorModel, db: Session = Depends(get_db)):
  db_administrador = AdministradorRepo.read_by_id(db, id_administrador)
  if db_administrador:
    update_administrador_encoded = jsonable_encoder(administrador_request)
    db_administrador.nome_completo = update_administrador_encoded['nome_completo']
    db_administrador.email = update_administrador_encoded['email']
    db_administrador.data_nascimento = update_administrador_encoded['data_nascimento']
    db_administrador.senha = update_administrador_encoded['senha']
    return await AdministradorRepo.update(db=db, administrador_data=db_administrador)
  else:
      raise HTTPException(status_code=400, detail="Administrador não consta em nossa banco de dados :c")

# CRUD DE CONTEUDO
@app.post('/conteudo', tags=["Conteudo"], response_model=schemas.ConteudoModel, status_code=201)
async def create_conteudo():
  pass
@app.get('/conteudo/{id}', tags=["Conteudo"], response_model=schemas.ConteudoModel)
def get_conteudo():
  pass
@app.delete('/conteudo{id}', tags=["Conteudo"],)
async def delete_conteudo():
  pass
@app.put('/conteudo/{id}', tags=["Conteudo"], response_model=schemas.ConteudoModel)
async def update_conteudo():
  pass

# CRUD DE COLABORADOR
@app.post('/colaborador', tags=["Colaborador"], response_model=schemas.ColaboradorModel, status_code=201)
async def create_colaborador():
  pass
@app.get('/colaborador/{id}', tags=["Colaborador"], response_model=schemas.ColaboradorModel)
def get_colaborador():
  pass
@app.delete('/colaborador/{id}', tags=["Colaborador"])
async def delete_colaborador():
  pass
@app.put('/colaborador/{id}', tags=["Colaborador"], response_model=schemas.ColaboradorModel)
async def update_colaborador():
  pass