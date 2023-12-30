from typing import List

import pandas as pd

from constants.dimensions import GRID_WIDTH, GRID_HEIGHT
from constants.keys import X, Y, STATE
from constants.states import START, END, NOT_VISITED, VISITED, OBSTACLE, PATH


class Node:

    def __init__(self, state: str, parent: (int, int)):
        self.state = state
        self.parent = parent


class Grid:

    def __init__(self, width=50, height=50):
        """"""

        self.width = width
        self.height = height
        self.data = [[Node(NOT_VISITED, None) for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

    def children(self, x: int, y: int) -> List:
        """"""

        children = []

        def add(i: int, j: int):
            if 0 <= i < self.width and 0 <= j < self.height:
                children.append((i, j))

        add(x - 1, y)
        add(x + 1, y)
        add(x, y - 1)
        add(x, y + 1)

        return children

    def get_xy(self, state: str) -> (int, int):
        """Get the xy coordinate of the first entry with the given state."""

        for i in range(self.width):
            for j in range(self.height):
                if self.data[i][j].state == state:
                    return i, j

    def get_state(self, x, y) -> str:
        return self.data[x][y].state

    def get_parent(self, x, y) -> (int, int):
        return self.data[x][y].parent

    def set_state(self, x: int, y: int, state: str):
        self.data[x][y].state = state

    def set_parent(self, x: int, y: int, parent: (int, int)):
        self.data[x][y].parent = parent

    def toggle_obstacle(self, x, y):
        """Toggle cell between obstacle and non-obstacle state. No-op if cell is START or END."""

        old_state = self.get_state(x, y)
        if old_state in [START, END]:
            return

        new_state = OBSTACLE if old_state != OBSTACLE else NOT_VISITED
        self.set_state(x, y, new_state)

    def toggle_visit(self, x, y):
        """Toggle cell between visit and non-visit state. No-op if cell is START, END or OBSTACLE."""

        old_state = self.get_state(x, y)
        if old_state in [START, END, OBSTACLE]:
            return

        new_state = VISITED if old_state != VISITED else NOT_VISITED
        self.set_state(x, y, new_state)

    def clear_visited(self):

        for i in range(self.width):
            for j in range(self.height):
                if self.data[i][j].state in [VISITED, PATH]:
                    self.data[i][j].state = NOT_VISITED
                    self.data[i][j].parent = None
                if self.data[i][j].state in [END, START]:
                    self.data[i][j].parent = None

    def clear_all(self):

        for i in range(self.width):
            for j in range(self.height):
                if self.data[i][j].state in [VISITED, OBSTACLE, PATH]:
                    self.data[i][j].state = NOT_VISITED
                    self.data[i][j].parent = None
                if self.data[i][j].state in [END, START]:
                    self.data[i][j].parent = None

    def toDataFrame(self) -> pd.DataFrame:

        xs = []
        ys = []
        states = []
        for i in range(self.width):
            for j in range(self.height):
                xs.append(i)
                ys.append(j)
                states.append(self.data[i][j].state)

        return pd.DataFrame({X: xs, Y: ys, STATE: states})
