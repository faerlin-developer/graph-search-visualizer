import math
from queue import PriorityQueue

from constants.states import START, END, NOT_VISITED, VISITED
from .graph import Grid


class AStar:

    def __init__(self, grid: Grid):
        self.queue = PriorityQueue()
        self.grid = grid

        start_x, start_y = grid.get_xy(START)
        self.queue.put((0, start_x, start_y, None))

        self.end_x, self.end_y = grid.get_xy(END)

        self.found = False

    def run(self) -> bool:

        while not self.queue.empty():

            _, x, y, parent = self.queue.get()
            state = self.grid.get_state(x, y)

            if state == END:
                self.found = True
                self.grid.set_parent(x, y, parent)
                break
            elif state in [START, NOT_VISITED]:

                for child_x, child_y in self.grid.children(x, y):
                    key = self.distance(child_x, child_y, self.end_x, self.end_y)
                    child_parent = (x, y)
                    self.queue.put((key, child_x, child_y, child_parent))

                if state == NOT_VISITED:
                    self.grid.set_state(x, y, VISITED)
                    self.grid.set_parent(x, y, parent)

        return self.found

    def distance(self, x0, y0, x1, y1) -> float:
        return math.sqrt(math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2))
