from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, create_engine

Base = declarative_base()

class Listing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key = True)
    title = Column(Text)
    housing = Column(Text)
    neighborhood = Column(Text)
    price = Column(Integer)
