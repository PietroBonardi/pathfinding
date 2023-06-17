from pathfinder.data_structure.map import Map
from pathfinder.engines.solver import Solver
from typing import List, Tuple
import random


class Node:
    def __init__(self, coordinate: Tuple[int, int], precursor=None) -> None:
        self.coordinate = coordinate
        self.precursor = precursor

    def extract_path(self) -> List[Tuple[int, int]]:
        if self.precursor == None:
            return [self.coordinate]
        else:
            return self.precursor.extract_path()+[self.coordinate]


class RandomWalk(Solver):
    def __init__(self, grid: Map) -> None:
        super().__init__(grid)

    def solve(self) -> List[Tuple[int, int]]:
        # Call solver algorithm
        final_node = self.random_walk()

        return final_node.extract_path()

    def random_walk(self) -> Node:
        start = self.grid.start
        end = self.grid.end
        current = Node(start)

        while True:
            if current.coordinate == end:
                return current

            successors = self.get_successors(current.coordinate)
            next = Node(random.sample(successors, 1)[0], current)
            current = next
