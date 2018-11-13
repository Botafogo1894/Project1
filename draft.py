def build_trace_all_players_points(title = 'Player Points vs Player Cost', type = 'scatter'):
    list_of_player_costs = [item.cost for item in player_list()]
    list_of_player_points = [item.total_points for item in player_list()]
    trace1 = dict(x = list_of_player_costs, y = list_of_player_points, type = type)
    layout = dict(title = title)
    return dict(data = [trace1], layout =layout)
