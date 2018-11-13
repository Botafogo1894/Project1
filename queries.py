from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///EPL_fantasy.db')

Session = sessionmaker(bind=engine)
session = Session()


def roi_top_players():
    return session.query(Player).order_by(Player.roi.desc()).all()

def points_top_players():
    return session.query(Player).order_by(Player.total_points.desc()).all()

def bonus_top_players():
    return session.query(Player).order_by(Player.bonus.desc()).all()

def players_by_status(status):
    return session.query(Player).filter(Player.status == status).all()

def roi_filter_by_position(position, number = 10):
    return session.query(Player).filter(Player.position == position).order_by(Player.roi.desc())[:number]

def points_filter_by_position(position, number = 10):
    return session.query(Player).filter(Player.position == position).order_by(Player.total_points.desc())[:number]

def team_list():
    return session.query(Team).all()

def player_list():
    return session.query(Player).all()


def build_team_by_roi(budget = 100, count_limit = 3, gk = 2, df = 5, md = 5, fwd = 3):
    money_team = []
    budget = budget
    injured = players_by_status('injured')
    positions = {'Goalkeeper': gk, 'Defender': df, 'Midfielder': md, 'Forward': fwd}
    for player in points_top_players():
            if len(money_team) < count_limit and player not in injured and budget >= player.cost and positions[player.position] > 0:
                money_team.append(player)
                budget -= player.cost
                positions[player.position] = positions[player.position] - 1
            else:
                for player in roi_top_players():
                    if player not in money_team and budget >= player.cost and positions[player.position] > 0:
                        money_team.append(player)
                        budget -= player.cost
                        positions[player.position] = positions[player.position] - 1
    print(budget)
    return money_team

def build_team_by_points(budget = 100, count_limit = 15, gk = 2, df = 5, md = 5, fwd = 3):
    money_team = []
    budget = budget
    injured = players_by_status('injured')
    positions = {'Goalkeeper': gk, 'Defender': df, 'Midfielder': md, 'Forward': fwd}
    for player in points_top_players():
            if len(money_team) < count_limit and player not in injured and budget >= player.cost and positions[player.position] > 0:
                money_team.append(player)
                budget -= player.cost
                positions[player.position] = positions[player.position] - 1
    print(budget)
    return money_team
