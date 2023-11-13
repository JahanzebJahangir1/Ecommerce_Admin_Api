from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Change credentials to according to user database
DB_NAME = 'e_admin_api'
DB_USER = 'root'
DB_PASSWORD = 'assassins312'
DB_HOST = 'localhost'
DB_PORT = '3306'

DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()