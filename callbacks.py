from dash import ctx
from dash.dependencies import Input, Output, State

from constants.ids import RUN_ID, CLEAR_ALL_ID, CLEAR_VISITED_ID, GRID_ID
from constants.options import ASTAR_OPTION, BFS_OPTION
from constants.options import MOVE_START_OPTION, MOVE_END_OPTION, MOVE_OBSTACLE_OPTION
from constants.states import START, END, PATH, NOT_VISITED
from graph import grid
from graph.a_star import AStar
from graph.bfs import BFS
from ui import app
from ui.figure import create_figure


@app.callback(
    Output('grid', 'figure'),
    [Input('grid', 'clickData'), Input('run', 'n_clicks'),
     Input('clear all', 'n_clicks'), Input('clear visited', 'n_clicks')],
    [State('algorithm', 'value'), State('modify state', 'value')]
)
def callback_grid(click_data, run_clicks, clear_visited_clicks, clear_all_clicks, algorithm, state_option):
    """"""

    if len(click_data) == 0 and run_clicks == 0 and clear_visited_clicks == 0 and clear_all_clicks == 0:
        return create_figure(grid.toDataFrame())

    triggered_id = ctx.triggered_id

    if triggered_id == RUN_ID:

        grid.clear_visited()

        if algorithm == ASTAR_OPTION:
            finder = AStar(grid)
        elif algorithm == BFS_OPTION:
            finder = BFS(grid)
        else:
            raise Exception(f"algorithm not supported: {algorithm}")

        found = finder.run()

        end_x, end_y = grid.get_xy(END)
        node = grid.get_parent(end_x, end_y)
        while node is not None:
            x, y = node
            if grid.get_state(x, y) != START:
                grid.set_state(x, y, PATH)
            node = grid.get_parent(x, y)

    if triggered_id == CLEAR_ALL_ID:
        grid.clear_all()

    if triggered_id == CLEAR_VISITED_ID:
        grid.clear_visited()

    if triggered_id == GRID_ID:

        point = click_data['points'][0]
        x, y = point['x'], point['y']
        state = grid.get_state(x, y)

        if state not in [START, END]:

            if state_option == MOVE_OBSTACLE_OPTION:
                grid.toggle_obstacle(x, y)

            if state_option == MOVE_START_OPTION:
                start_x, start_y = grid.get_xy(START)
                grid.set_state(start_x, start_y, NOT_VISITED)
                grid.set_state(x, y, START)

            if state_option == MOVE_END_OPTION:
                end_x, end_y = grid.get_xy(END)
                grid.set_state(end_x, end_y, NOT_VISITED)
                grid.set_state(x, y, END)

    return create_figure(grid.toDataFrame())
