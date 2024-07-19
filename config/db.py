from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS__1cZtouYw6xF5XKhFir@mysql-167320d6-carloshernandez74199-f967.e.aivencloud.com:23040/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()