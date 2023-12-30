from constants.coordinates import START_X, START_Y, END_X, END_Y
from constants.dimensions import GRID_WIDTH, GRID_HEIGHT
from constants.states import START, END
from . import graph

grid = graph.Grid(GRID_WIDTH, GRID_HEIGHT)
grid.set_state(START_X, START_Y, START)
grid.set_state(END_X, END_Y, END)
