from map import Map
from solver import Solver

class Node:

    def __init__(self, state) -> None:
        self.state = state

class BFS(Solver):

    def __init__(self, grid: Map):
        super().__init__(grid)
        self.start = grid.start
        self.goal = grid.end
        self.frontier = [self.start]
        self.explored = []

    def is_goal(self, node: Node):
        return node.state == self.goal

    def solve(self):
        pass
        # while self.frontier != []:
        #     current_node = self.frontier.pop(0)
            
        #     if self.is_goal(current_node):
        #         return current_node
            
        #     self.explored.append(current_node)
        #     for neighbor in self.grid.get_successors(current_node):
        #         pass
    
