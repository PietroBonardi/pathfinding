from map import Map
from solver import Solver
from typing import List,Tuple

class Node:
    def __init__(self, state) -> None:
        self.state = state

class DepthFirstSearch(Solver):

    def __init__(self, grid: Map) -> None:
        super().__init__(grid)

    def solve(self) -> List[Tuple[int,int]]:
        # Call solver algorithm
        something = self.run_dfs()
        
        return 

    def dfs_algorithm():
        # Do stuff
        


        pass