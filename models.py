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
    status = Column(String)
    transfers_out = Column(Integer)
    transfers_in = Column(Integer)

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key = True)
    # table_id = Column(Integer, Foreign_Key('epl_table.id'))
    code = Column(Integer)
    position = Column(Integer)
    name = Column(String)
    logo = Column(String)
    games_played = Column(Integer)
    W = Column(Integer)
    D = Column(Integer)
    L = Column(Integer)
    points = Column(Integer)
    GF = Column(Integer)
    GA = Column(Integer)
    GD = Column(Integer)
    player_points = Column(Integer)
    players = relationship('Player', back_populates = 'team')

# class Table(Base):
#     __tablename__ = "epl_table"
#     id = Column(Integer, primary_key = True)
#     position = relationship('Team', back_populates = 'position')
#     teams = relationship('Team', back_populates = 'team')
