from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.users_roles, config.db, schemas.users_roles, models.users_roles
from typing import List
from portadortoken import Portador


users_roles = APIRouter()

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@users_roles.get("/users_roles/", response_model=List[schemas.users_roles.UserRol], tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def read_users_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users_roles= crud.users_roles.get_users_roles(db=db, skip=skip, limit=limit)
    return db_users_roles

@users_roles.post("/users_roles/{id_user}/{id_rol}", response_model=schemas.users_roles.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def read_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol= crud.users_roles.get_userrol(db=db, id_user=id_user,id_rol=id_rol)

    if db_userrol is None:
        raise HTTPException(status_code=404, detail="UserRol no existe")
    return db_userrol


@users_roles.post("/users_roles/", response_model=schemas.users_roles.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def create_user(userrol: schemas.users_roles.UserRolCreate, db: Session = Depends(get_db)):
    db_userrol = crud.users_roles.get_userrol(db=db, id_user=userrol.Usuario_ID, id_rol=userrol.Rol_ID)
    print (db_userrol)
    if db_userrol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.users_roles.create_userrol(db=db, userrol=userrol)
    # return crud.users_roles.create_userrol(db=db, userrol=userrol)

@users_roles.put("/users_roles/{id_user}/{id_rol}", response_model=schemas.users_roles.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def update_user(id_user: int, id_rol: int, userrol: schemas.users_roles.UserRolUpdate, db: Session = Depends(get_db)):
    db_userrol = crud.users_roles.update_userrol(db=db, id_user=id_user, id_rol=id_rol, userrol=userrol)
    
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    
    # Ahora es seguro acceder a los atributos de db_userrol
    print(db_userrol.Estatus)
    
    return db_userrol


@users_roles.delete("/users_roles/{id_user}/{id_rol}", response_model=schemas.users_roles.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def delete_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol = crud.users_roles.delete_userrol(db=db, id_user=id_user, id_rol=id_rol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_userrol