from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.persons,config.db,schemas.persons,models.persons
from typing import List

person = APIRouter()

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@person.get("/persons/", response_model=List[schemas.persons.Person], tags=["Personas"] ,dependencies=[Depends(Portador())])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persons= crud.persons.get_persons(db=db, skip=skip, limit=limit)
    return db_persons

@person.post("/person/{ID}", response_model=schemas.persons.Person, tags=["Personas"] ,dependencies=[Depends(Portador())])
def read_person(ID: int, db: Session = Depends(get_db)):
    db_person= crud.persons.get_person(db=db, ID=ID)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@person.post("/persons/", response_model=schemas.persons.Person, tags=["Personas"])
def create_person(person: schemas.persons.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person_by_Nombre(db, Nombre=person.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)

@person.put("/person/{ID}", response_model=schemas.persons.Person, tags=["Personas"] ,dependencies=[Depends(Portador())])
def update_person(ID: int, person: schemas.persons.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.persons.update_person(db = db, ID = ID, person = person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existente, no esta actuaizado")
    return db_person

@person.delete("/person/{ID}", response_model=schemas.persons.Person, tags=["Personas"] ,dependencies=[Depends(Portador())])
def delete_person(ID: int, db: Session = Depends(get_db)):
    db_person = crud.persons.delete_person(db = db, ID = ID)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_person