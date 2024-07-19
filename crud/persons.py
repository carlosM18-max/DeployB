import models.persons
import schemas.persons
from sqlalchemy.orm import Session

def get_person(db:Session, ID:int):
    return db.query(models.persons.Person).filter(models.persons.Person.ID == ID).first()

def get_person_by_Nombre(db: Session, Nombre: str):
    return db.query(models.persons.Person).filter(models.persons.Person == Nombre).first()

def get_persons(db: Session, skip:int=0,limit:int=10):
    return db.query(models.persons.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person:schemas.persons.PersonCreate):
    db_person = models.persons.Person(Titulo_Cortesia=person.Titulo_Cortesia,Nombre=person.Nombre, Primer_Apellido=person.Primer_Apellido, Segundo_Apellido=person.Segundo_Apellido,Curp=person.Curp,Genero=person.Genero,Tipo_Sangre=person.Tipo_Sangre,Fecha_Nacimiento=person.Fecha_Nacimiento,Fotografia=person.Fotografia,Telefono=person.Telefono,Correo_Electronico=person.Correo_Electronico,Estatus=person.Estatus, Fecha_Registro=person.Fecha_Registro,Fecha_Actualizacion=person.Fecha_Actualizacion )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, ID: int, person: schemas.persons.PersonUpdate):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.ID == ID).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, ID: int):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.ID == ID).first()
    if  db_person:
        db.delete(db_person)
        db.commit()
    return db_person
