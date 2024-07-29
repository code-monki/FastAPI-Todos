from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

''' defines location of database '''
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234@localhost/TodoApplicationDatabase'

''' create database engine connection '''

''' SQLite only '''
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


engine = create_engine(SQLALCHEMY_DATABASE_URL)

''' create session local '''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

