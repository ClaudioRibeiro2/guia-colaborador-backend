from sqlalchemy.orm import Session
from . import models, schemas

class AdministradorRepo:
  async def create(db: Session, administrador: schemas.AdministradorModel):
    db_administrador = models.AdministradorBase(nome_completo=administrador.nome_completo,
                                                email=administrador.email,
                                                data_nascimento=administrador.data_nascimento,
                                                senha=administrador.senha)
    db.add(db_administrador)
    db.commit()
    db.refresh(db_administrador)
    return db_administrador
  
  def read_by_id(db: Session, id_administrador):
    return db.query(models.AdministradorBase).filter_by(id_administrador = id_administrador).first()
  
  def read_by_email(db: Session, email):
    return db.query(models.AdministradorBase).filter_by(email = email).first()

  async def update(db: Session, administrador_data):
    updated_item = db.merge(administrador_data)
    db.commit()
    return updated_item
  
  async def delete(db: Session, id_administrador):
    db_item = db.get(models.AdministradorBase ,id_administrador)
    db.delete(db_item)
    db.commit()
  
  
class ColaboradorRepo:
  async def create(db: Session, colaborador: schemas.ColaboradorModel):
    db_colaborador = models.ColaboradorBase(nome_completo=colaborador.nome_completo,
                                            email=colaborador.email,
                                            data_nascimento=colaborador.data_nascimento,
                                            senha=colaborador.senha,
                                            id_administrador=colaborador.id_administrador)
    db.add(db_colaborador)
    db.commit()
    db.refresh(db_colaborador)
    return db_colaborador
  
  def read_by_id(db: Session, id_colaborador):
    return db.query(models.ColaboradorBase).filter_by(id_colaborador = id_colaborador).first()

  def read_by_email(db: Session, email):
    return db.query(models.ColaboradorBase).filter_by(email = email).first()
  
  async def update(db: Session, colaborador_data):
    updated_colaborador = db.merge(colaborador_data)
    db.commit()
    return updated_colaborador
  
  async def delete(db: Session, id_colaborador):
    db_item = db.get(models.ColaboradorBase , id_colaborador)
    db.delete(db_item)
    db.commit()
  

class ConteudoRepo:
  async def create(db: Session, conteudo: schemas.ConteudoModel):
    db_conteudo = models.ConteudoBase(nome_completo=conteudo.titulo,
                                      email=conteudo.tipo,
                                      data_nascimento=conteudo.corpo,
                                      id_administrador=conteudo.id_administrador)
    db.add(db_conteudo)
    db.commit()
    db.refresh(db_conteudo)
    return db_conteudo

  def read_by_id_administrador(db: Session, id_administrador):
    return db.query(models.ConteudoBase).filter_by(id_administrador = id_administrador).first() 
  
  def read_by_titulo(db: Session, titulo:str):
    return db.query(models.ConteudoBase).filter_by(titulo = titulo).first()
  
  def read_by_conteudos(db: Session, id_administradora:int):
    return db.query(models.ConteudoBase).filter_by(id_administradora = id_administradora).all()
  
  def read_by_id_conteudo(db: Session, id_conteudo:int):
    return db.query(models.ConteudoBase).filter_by(id_conteudo = id_conteudo)
  
  async def update(db: Session, conteudo_data):
    print(conteudo_data)
    updated_conteudo = db.merge(conteudo_data)
    db.commit()
    return updated_conteudo
  
  async def delete(db: Session, id_conteudo):
    db_item = db.get(models.AdministradorBase , id_conteudo)
    db.delete(db_item)
    db.commit()