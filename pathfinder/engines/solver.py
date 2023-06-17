from pathfinder.data_structure.map import Map
from pathfinder.shortcuts import *
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
        """
            Add comments.
        """
        i, j = coordinates
        successor = []
        lower_i = max(i-1, 0)
        upper_i = min(i+1, self.grid.row-1)
        lower_j = max(j-1, 0)
        upper_j = min(j+1, self.grid.col-1)
        for next_i in range(lower_i, upper_i+1):
            for next_j in range(lower_j, upper_j+1):
                if not (next_i == i and next_j == j):
                    if self.grid.get_element((next_i, next_j)) != OBSTACLE:
                        successor.append((next_i, next_j))

        return successor
