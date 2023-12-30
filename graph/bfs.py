from collections import deque

from constants.states import START, END, NOT_VISITED, VISITED
from .graph import Grid


class BFS:

    def __init__(self, grid: Grid):
        self.queue = deque()
        self.grid = grid

        x, y = grid.get_xy(START)
        self.queue.append((x, y, None))

        self.found = False

    def run(self) -> bool:

        while len(self.queue) != 0:

            x, y, parent = self.queue.popleft()
            state = self.grid.get_state(x, y)

            if state == END:
                self.found = True
                self.grid.set_parent(x, y, parent)
                break
            elif state in [START, NOT_VISITED]:

                for child_x, child_y in self.grid.children(x, y):
                    child_parent = (x, y)
                    self.queue.append((child_x, child_y, child_parent))

                if state == NOT_VISITED:
                    self.grid.set_state(x, y, VISITED)
                    self.grid.set_parent(x, y, parent)

        return self.found
