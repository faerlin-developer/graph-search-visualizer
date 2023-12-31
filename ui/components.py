import dash_bootstrap_components as dbc
from dash import html

from constants.ids import ALGORITHM_ID
from constants.ids import MODIFY_STATE_ID, RUN_ID, CLEAR_ALL_ID, CLEAR_VISITED_ID
from constants.options import ASTAR_OPTION, BFS_OPTION
from constants.options import MOVE_START_OPTION, MOVE_END_OPTION, MOVE_OBSTACLE_OPTION

paragraph1 = html.Div(
    'Click the RUN button to determine a path from the start cell to the end cell. '
    'This path will consists of green cells. '
    'Cells that are visited by the search algorithm are blue. '
    'Obstacle cells are black.',
    style={'font-size': '14px'})

paragraph2 = html.Div(
    'Clicking on a grid cell allows you to modify its state: '
    'add or remove an obstacle cell, move the start cell, and move the end cell.',
    style={'font-size': '14px'})

modify_cell_radio = html.Div(
    [
        dbc.Label("Modify Grid Cell", style={'font-weight': 'bold'}),
        dbc.RadioItems(id=MODIFY_STATE_ID,
                       options=[MOVE_OBSTACLE_OPTION, MOVE_START_OPTION, MOVE_END_OPTION],
                       value=MOVE_OBSTACLE_OPTION)
    ]
)

select_algorithm_radio = html.Div(
    [
        dbc.Label("Select Search Algorithm", style={'font-weight': 'bold'}),
        dbc.RadioItems(id=ALGORITHM_ID,
                       options=[ASTAR_OPTION, BFS_OPTION],
                       value=ASTAR_OPTION),
    ]
)

run_buttons = html.Div(
    dbc.ButtonGroup(
        [
            dbc.Button("RUN", id=RUN_ID, color="success", n_clicks=0),
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem("Visited", id=CLEAR_VISITED_ID, n_clicks=0),
                    dbc.DropdownMenuItem("Visited and Obstacles", id=CLEAR_ALL_ID, n_clicks=0)
                ],
                label="Clear Cells",
                group=True,
            ),
        ],
        vertical=True
    ),
    className="d-grid gap-2 col-6 mx-auto"
)
