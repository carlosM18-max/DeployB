from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class UserRol(Base):
    __tablename__ = "tbd_users_roles"

    Usuario_ID = Column(Integer, ForeignKey("tbb_users.ID"), primary_key=True)
    Rol_ID = Column(Integer, ForeignKey("tbc_roles.ID"), primary_key=True)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)