from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import models, schemas
from db import  engine


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
async def create_administrador():
  pass
@app.get('/administrador/{id}', tags=["Administrador"], response_model=schemas.AdministradorModel)
def get_administrador():
  pass
@app.delete('/administrador/{id}', tags=["Administrador"])
async def delete_administrador():
  pass
@app.put('/administrador/{id}', tags=["Administrador"], response_model=schemas.AdministradorModel)
async def update_administrador():
  pass

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