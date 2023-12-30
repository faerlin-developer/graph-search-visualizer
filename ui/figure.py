import plotly.express as px

from constants.dimensions import FIGURE_WIDTH, FIGURE_HEIGHT
from constants.keys import X, Y, STATE
from constants.states import START, END, NOT_VISITED, VISITED, OBSTACLE, PATH

color_discrete_map = {
    START: 'green',
    END: 'green',
    NOT_VISITED: 'white',
    VISITED: 'blue',
    OBSTACLE: 'black',
    PATH: 'green'}

symbol_map = {
    START: 'circle-x',
    END: 'star',
    NOT_VISITED: 'square',
    VISITED: 'square',
    OBSTACLE: 'square',
    PATH: 'square'}


def create_figure(data):
    """"""

    figure = px.scatter(data_frame=data,
                        x=X, y=Y,
                        color=STATE, symbol=STATE,
                        color_discrete_map=color_discrete_map, symbol_map=symbol_map,
                        width=FIGURE_WIDTH, height=FIGURE_HEIGHT,
                        template='simple_white')

    line = dict(width=1, color='rgb(128,128,128)')
    marker = dict(size=15, line=line)
    selector = dict(mode='markers')
    figure.update_traces(marker=marker, selector=selector)
    figure.update_traces(hovertemplate=None)
    figure.update_layout(yaxis_visible=False, yaxis_showticklabels=False,
                         xaxis_visible=False, xaxis_showticklabels=False,
                         xaxis_fixedrange=True, yaxis_fixedrange=True,
                         showlegend=True)
    figure.update_layout(legend=dict(orientation="h", xanchor="right", yanchor="top", x=0.95, y=1.0))

    return figure
