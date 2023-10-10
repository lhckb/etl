from sqlalchemy import Column, Integer, String, BigInteger, Double, UUID, create_engine
from sqlalchemy.ext.declarative import declarative_base
import uuid

database = "postgres"
user = "postgres"
host = "0.0.0.0"
password = "password"
port = 5433

conn_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(conn_string)

Base = declarative_base()

class DictionaryOlympics(Base):
    __tablename__ = 'dictionary_olympics'
    country = Column(String)
    code = Column(String(3), primary_key=True, unique=True, nullable=False)
    population = Column(BigInteger)
    gdp_per_capita = Column(Double)
  
class SummerOlympics(Base):
    __tablename__ = 'summer_olympics'
    country = Column(String)
    code = Column(String(3), primary_key=True, unique=True, nullable=False)
    population = Column(BigInteger)
    gdp_per_capita = Column(Double)

class WinterOlympics(Base):
    __tablename__ = 'winter_olympics'
    country = Column(String)
    code = Column(String(3), primary_key=True, unique=True, nullable=False)
    population = Column(BigInteger)
    gdp_per_capita = Column(Double)

def createTables():
  Base.metadata.create_all(engine)
