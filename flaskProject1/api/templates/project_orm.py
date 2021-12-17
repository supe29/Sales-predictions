import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import column, String, Integer, Float
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base()

#main code

class Userinput(Base):
    __tablename__= "userinputs"