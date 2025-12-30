from pathfinding.data_structure.map import Map


class Solver:  # NOTE: Abstract method
    def __init__(self, map: Map) -> None:
        self.map = map

    def solve(self):
        raise NotImplementedError
