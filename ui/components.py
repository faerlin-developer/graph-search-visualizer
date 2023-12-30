import dash_bootstrap_components as dbc
from dash import html

from constants.ids import ALGORITHM_ID
from constants.ids import MODIFY_STATE_ID, RUN_ID, CLEAR_ALL_ID, CLEAR_VISITED_ID
from constants.options import ASTAR_OPTION, BFS_OPTION
from constants.options import MOVE_START_OPTION, MOVE_END_OPTION, MOVE_OBSTACLE_OPTION

intro_div = html.Div(
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
    'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s. '
    'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s.',
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
            dbc.Button("Run", id=RUN_ID, color="success", n_clicks=0),
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
