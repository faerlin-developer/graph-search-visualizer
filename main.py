import logging

import dash_bootstrap_components as dbc
from dash import dcc, html

from callbacks import handler
from constants.ids import GRID_ID
from graph import grid
from ui import app
from ui.components import paragraph1, paragraph2, modify_cell_radio, select_algorithm_radio, run_buttons
from ui.figure import create_figure


def main():
    """Initialize the layout of the dash application and run server."""

    card = dbc.Card(
        [
            paragraph1,
            html.Br(),
            paragraph2,
            html.Hr(),
            modify_cell_radio,
            select_algorithm_radio,
            html.Hr(),
            run_buttons
        ],
        body=True,
    )

    graph = dcc.Graph(
        id=GRID_ID,
        figure=create_figure(grid.toDataFrame()),
        clickData={},
        hoverData={},
        config=dict(displayModeBar=False)
    ),

    app.layout = dbc.Container(
        [
            html.H1("Graph Search Algorithms"),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(card, md=4),
                    dbc.Col(graph, md=8),
                ],
                align="center"
            ),
        ],
        fluid=True
    )

    log_callbacks()
    app.run_server()


def log_callbacks():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.info(f"added dash callback {handler.__name__}")


if __name__ == '__main__':
    main()
