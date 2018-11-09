from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key = True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates = 'players')
    team_code = Column(Integer)
    name = Column(String)
    position = Column(String)
    cost = Column(Float)
    total_points = Column(Integer)
    roi = Column(Float)
    bonus = Column(Integer)
    red_cards = Column(Integer)
    minutes = Column(Integer)
    transfers_out = Column(Integer)
    transfers_in = Column(Integer)

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    code = Column(Integer)
    player_points = Column(Integer)
    table_points = Column(Integer)
    table_position = Column(Integer)
    players = relationship('Player', back_populates = 'team')
