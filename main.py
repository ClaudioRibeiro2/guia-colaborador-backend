from typing import List
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
  db_administrador = AdministradorRepo.read_by_email(db, email=administrador_request.email)
  print(db_administrador)
  if db_administrador:
        raise HTTPException(status_code=400, detail="Já existe um Administrador com esse e-mail!")
  return await AdministradorRepo.create(db=db, administrador=administrador_request)

@app.get('/administrador/id/{id_administrador}', tags=["Administrador"], response_model=schemas.AdministradorResponseModel)
def get_administrador(id_administrador: int, db: Session = Depends(get_db)):
  db_administrador = AdministradorRepo.read_by_id(db, id_administrador)
  if db_administrador is None:
    raise HTTPException(status_code=404, detail="Administrador não consta em nossa banco de dados :c")
  return db_administrador

@app.get('/administrador/all', tags=["Administrador"], response_model=List[schemas.AdministradorResponseModel])
def get_all_administrador(db: Session = Depends(get_db)):
  db_administrador = AdministradorRepo.read_all(db)
  return db_administrador

@app.delete('/administrador/{id_administrador}', tags=["Administrador"])
async def delete_administrador(id_administrador: int, db: Session = Depends(get_db)):
  db_administrador = AdministradorRepo.read_by_id(db, id_administrador)
  if db_administrador is None:
    raise HTTPException(status_code=404, detail="Administrador não consta em nossa banco de dados :c")
  await AdministradorRepo.delete(db, id_administrador)
  return "Administrador removido com sucesso!"

@app.put('/administrador/{id_administrador}', tags=["Administrador"], response_model=schemas.AdministradorResponseModel)
async def update_administrador(id_administrador: int, administrador_request: schemas.AdministradorModel, db: Session = Depends(get_db)):
  db_administrador = db.get(models.AdministradorBase, id_administrador)
  if db_administrador:
    # update_administrador_encoded = jsonable_encoder(administrador_request)
    db_administrador.nome_completo = administrador_request.nome_completo
    db_administrador.email = administrador_request.email
    db_administrador.setor = administrador_request.setor
    db_administrador.data_nascimento = administrador_request.data_nascimento
    db_administrador.senha = administrador_request.senha
    return await AdministradorRepo.update(db=db, administrador_data=db_administrador)
  else:
      raise HTTPException(status_code=400, detail="Administrador não consta em nossa banco de dados :c")

# CRUD DE COLABORADOR
@app.post('/colaborador', tags=["Colaborador"], response_model=schemas.ColaboradorModel, status_code=201)
async def create_colaborador(colaborador_request: schemas.ColaboradorModel, db: Session = Depends(get_db)):
  db_colaborador = ColaboradorRepo.read_by_email(db, email=colaborador_request.email)
  if db_colaborador:
        raise HTTPException(status_code=400, detail="Este colaborador já existe!")
  return await ColaboradorRepo.create(db=db, colaborador=colaborador_request)

@app.get('/colaborador/all', tags=["Colaborador"], response_model=List[schemas.ColaboradorResponseModel])
def get_all_colaborador(db: Session = Depends(get_db)):
  db_colaborador = ColaboradorRepo.read_all(db)
  return db_colaborador

@app.get('/colaborador/id/{id_colaborador}', tags=["Colaborador"], response_model=schemas.ColaboradorResponseModel)
def get_colaborador(id_colaborador: int, db: Session = Depends(get_db)):
  db_colaborador = ColaboradorRepo.read_by_id(db, id_colaborador)
  if db_colaborador is None:
    raise HTTPException(status_code=404, detail="Conteudo não consta em nossa banco de dados :c")
  return db_colaborador

@app.delete('/colaborador/{id_colaborador}', tags=["Colaborador"])
async def delete_colaborador(id_colaborador: int, db: Session = Depends(get_db)):
  db_conteudo = ColaboradorRepo.read_by_id(db, id_colaborador)
  if db_conteudo is None:
    raise HTTPException(status_code=404, detail="Colaborador não consta em nossa banco de dados :c")
  await ColaboradorRepo.delete(db, id_colaborador)
  return "Colaborador removido com sucesso!"

@app.put('/colaborador/{id_colaborador}', tags=["Colaborador"], response_model=schemas.ColaboradorResponseModel)
async def update_colaborador(id_colaborador: int, colaborador_request: schemas.ColaboradorModel, db: Session = Depends(get_db)):
  db_colaborador = db.get(models.ColaboradorBase, id_colaborador)
  if db_colaborador:
    db_colaborador.nome_completo = colaborador_request.nome_completo
    db_colaborador.email = colaborador_request.email
    db_colaborador.setor = colaborador_request.setor
    db_colaborador.data_nascimento = colaborador_request.data_nascimento
    db_colaborador.senha = colaborador_request.senha
    db_colaborador.id_administrador = colaborador_request.id_administrador
    return await ColaboradorRepo.update(db=db, colaborador_data=db_colaborador)
  else:
      raise HTTPException(status_code=400, detail="Colaborador não consta em nossa banco de dados :c")


# CRUD DE CONTEUDO
@app.post('/conteudo', tags=["Conteudo"], response_model=schemas.ConteudoModel, status_code=201)
async def create_conteudo(conteudo_request: schemas.ConteudoModel, db: Session = Depends(get_db)):
  return await ConteudoRepo.create(db=db, conteudo=conteudo_request)

@app.get('/conteudo/id/{id_conteudo}', tags=["Conteudo"], response_model=schemas.ConteudoResponseModel)
def get_conteudo(id_conteudo: int, db: Session = Depends(get_db)):
  db_conteudo = ConteudoRepo.read_by_id_conteudo(db, id_conteudo)
  if db_conteudo is None:
    raise HTTPException(status_code=404, detail="Conteudo não consta em nossa banco de dados :c")
  return db_conteudo

@app.get('/conteudo/all', tags=["Conteudo"], response_model=List[schemas.ConteudoResponseModel])
def get_all_conteudo(db: Session = Depends(get_db)):
  db_conteudo = ConteudoRepo.read_all(db)
  return db_conteudo

@app.delete('/conteudo/{id_conteudo}', tags=["Conteudo"],)
async def delete_conteudo(id_conteudo: int, db: Session = Depends(get_db)):
  db_conteudo = ConteudoRepo.read_by_id_conteudo(db, id_conteudo)
  if db_conteudo is None:
    raise HTTPException(status_code=404, detail="Conteudo não consta em nossa banco de dados :c")
  await AdministradorRepo.delete(db, id_conteudo)
  return "Conteudo removido com sucesso!"
@app.put('/conteudo/{id_conteudo}', tags=["Conteudo"], response_model=schemas.ConteudoModel)
async def update_conteudo(id_conteudo: int, conteudo_request: schemas.ConteudoModel, db: Session = Depends(get_db)):
  db_conteudo = db.get(models.ConteudoBase, id_conteudo)
  if db_conteudo:
    db_conteudo.titulo = conteudo_request.titulo
    db_conteudo.tipo = conteudo_request.tipo
    db_conteudo.corpo = conteudo_request.corpo
    db_conteudo.id_administrador = conteudo_request.id_administrador
    return await ColaboradorRepo.update(db=db, colaborador_data=db_conteudo)
  else:
      raise HTTPException(status_code=400, detail="Conteudo não consta em nossa banco de dados :c")
