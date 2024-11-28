from datetime import date, datetime
from enum import Enum
import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db import Base;
    
class AdministradorBase(Base):
    __tablename__ = "administrador"

    id_administrador: Mapped[int] = mapped_column(sa.Integer, 
                                          primary_key=True,
                                          nullable=False,
                                          autoincrement=True)
    nome_completo: Mapped[str] = mapped_column(sa.String,
                                                nullable=False)
    email: Mapped[str] = mapped_column(sa.String,
                                    nullable=False,
                                    unique=True)
    data_nascimento: Mapped[datetime] = mapped_column(sa.DateTime(),
                             nullable=False)
    senha: Mapped[str] = mapped_column(sa.String,
                                    nullable=False)

class ColaboradorBase(Base):
    __tablename__ = "colaborador"

    id_colaborador: Mapped[int] = mapped_column(sa.Integer,
                                                primary_key=True,
                                                nullable=False,
                                                autoincrement=True)
    nome_completo: Mapped[str] = mapped_column(sa.String,
                                               nullable=False)
    email: Mapped[str] = mapped_column(sa.String,
                                       nullable=False)
    data_nascimento: Mapped[datetime] = mapped_column(sa.DateTime(),
                                                  nullable=False)
    senha: Mapped[str] = mapped_column(sa.String,
                                       nullable=False)
    id_administrador: Mapped[int] = mapped_column(sa.Integer(),
                                                  sa.ForeignKey('administrador.id_administrador'),
                                                  nullable=False)
    administrador: Mapped['AdministradorBase'] = relationship()    
    
class ConteudoBase(Base):
    __tablename__ = "conteudo"

    id_conteudo: Mapped[int] = mapped_column(sa.Integer,
                                             primary_key=True,
                                             nullable=False,
                                             autoincrement=True)
    titulo: Mapped[str] = mapped_column(sa.String,
                                        nullable=False)
    tipo: Mapped[str] = mapped_column(sa.Enum('BOAS_VINDAS', 'TO_DO','SOBRE_EMPRESA','DOCUMENTOS_IMPORTANTES'),
                                      default='DOCUMENTOS_IMPORTANTES',
                                      nullable=False)
    corpo: Mapped[str] = mapped_column(sa.String,
                                       nullable=False)
    id_administrador: Mapped[int] = mapped_column(sa.Integer(),
                                                  sa.ForeignKey('administrador.id_administrador'))
    administrador: Mapped['AdministradorBase'] = relationship()