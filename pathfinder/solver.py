from pathfinder.map import Map
from typing import Tuple


class Solver:
    def __init__(self, grid: Map) -> None:
        self.grid = grid

        pass

    def solve(self):
        """
        Entrypoint. 
        """
        raise NotImplementedError

    def get_successors(self, coordinates: Tuple[int, int]):
        i, j = coordinates
        successor = []
        start_x   = max(i-1,0)
        end_x     = min(i+1, self.grid.row-1)
        start_y   = max(j-1,0)
        end_y     = min(j+1, self.grid.col-1)
        for next_i in range(start_x,end_x+1):
            for next_j in range(start_y,end_y+1):
                if not (next_i == i and next_j == j):
                    if self.grid.get_element((next_i, next_j)) != self.grid.OBSTACLE:
                        successor.append((next_i, next_j))

        return successor
