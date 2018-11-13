import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from models import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from IPython.display import Image, HTML
from dash.dependencies import Input, Output, State
from queries import *

engine = create_engine('sqlite:///EPL_fantasy.db')

Session = sessionmaker(bind=engine)
session = Session()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_sql_table('teams', engine)

def generate_table(dataframe, max_rows=20):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns[2:]])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns[2:]
        ]) for i in range(min(len(dataframe), max_rows))]
    )

teamnames = [item.name for item in team_list()]
team_player_points = [item.player_points for item in team_list()]

app.layout = html.Div([
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Player Points Per Team', children=[
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': teamnames, 'y': team_player_points,
                                'type': 'bar', 'name': 'Player Points'}
                        ]
                    }
                )
            ])
        ]),
        dcc.Tab(label='EPL Table', children=[
            html.H4(children='Premier League Table'),
                generate_table(df),
                        ]
                ),
        dcc.Tab(label='Tab three', children=[
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [2, 4, 3],
                                'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [5, 4, 3],
                             'type': 'bar', 'name': u'Montréal'},
                        ]
                    }
                )
        ]),
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)

#
# app.layout = html.Div(children=[
#     html.H4(children='Premier League Table'),
#     generate_table(df)
# ])
