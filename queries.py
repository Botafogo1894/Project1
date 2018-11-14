from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///EPL_fantasy.db')

Session = sessionmaker(bind=engine)
session = Session()


def roi_top_players():
    return session.query(Player).order_by(Player.roi.desc()).all()

def roi_bottom_players():
    return session.query(Player).order_by(Player.roi).all()

def average__player_roi():
    return round(float(session.query(func.avg(Player.roi)).first()[0]), 2)

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
    count_limit = count_limit
    gk = gk
    df = df
    md = md
    fwd = fwd
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
    final_team = [(item.name, item.position, item.cost) for item in money_team]
    total_points = sum([item.total_points for item in money_team])
    print('Remaining Budget: ' + str(round(budget, 2)))
    print('Your AI has picked the following team:')
    print('GK: '), print([(item[0], item[2]) for item in final_team if item[1] == "Goalkeeper"])
    print('DF: '), print([(item[0], item[2]) for item in final_team if item[1] == "Defender"])
    print('MD: '), print([(item[0], item[2])  for item in final_team if item[1] == "Midfielder"])
    print('FWD: '), print([(item[0], item[2])  for item in final_team if item[1] == "Forward"])
    print('Total Fantasy Points: ' + str(total_points))
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
    final_team = [(item.name, item.position, item.cost) for item in money_team]
    total_points = sum([item.total_points for item in money_team])
    print('Remaining Budget: ' + str(round(budget, 2)))
    print('AVG Joe has picked the following team:')
    print('GK: '), print([(item[0], item[2]) for item in final_team if item[1] == "Goalkeeper"])
    print('DF: '), print([(item[0], item[2]) for item in final_team if item[1] == "Defender"])
    print('MD: '), print([(item[0], item[2])  for item in final_team if item[1] == "Midfielder"])
    print('FWD: '), print([(item[0], item[2])  for item in final_team if item[1] == "Forward"])
    print('Total Fantasy Points: ' + str(total_points))
    return money_team
