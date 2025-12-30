from pathfinder.data_structure.map import Map
from pathfinder.engines.solver import Solver
from typing import List, Tuple
import random


class Node:
    def __init__(self, coordinate: Tuple[int, int], precursor=None) -> None:
        self.coordinate = coordinate
        self.precursor = precursor

    def extract_path(self) -> List[Tuple[int, int]]:
        if self.precursor:
            return self.precursor.extract_path() + [self.coordinate]
        else:
            return [self.coordinate]
            


class RandomWalk(Solver):
    def __init__(self, map: Map) -> None:
        super().__init__(map)
        
    def solve(self) -> List[Tuple[int, int]]:
        final_node = self.random_walk()

        return final_node.extract_path()

    def random_walk(self) -> Node:
        start = self.map.start
        end = self.map.end
        current = Node(start)

        while True:
            if current.coordinate == end:
                return current

            successors = self.map.get_neighbor_coordinates(current.coordinate)
            next = Node(coordinate=random.sample(successors, 1)[0], precursor=current)
            current = next


class DepthFirstSearch(Solver):
    def __init__(self, map: Map) -> None:
        super().__init__(map)

    def solve(self) -> List[Tuple[int, int]]:
        final_node = self.dfs()

        return final_node.extract_path()

    def dfs(self) -> Node:
        start = self.map.start
        end = self.map.end

        closed = set()
        open = [Node(start)]

        while open:
            cur_node = open.pop()
            closed.add(cur_node.coordinate)

            if cur_node.coordinate == end:
                return cur_node

            successors = self.map.get_neighbor_coordinates(cur_node.coordinate)
            for coordinate in successors:
                if coordinate not in closed:
                    open.append(Node(coordinate=coordinate, precursor=cur_node))

        print("No solution found")


class BreadthFirstSearch(Solver):
    def __init__(self, map: Map) -> None:
        super().__init__(map)

    def solve(self) -> List[Tuple[int, int]]:
        final_node = self.bfs()

        return final_node.extract_path()

    def bfs(self) -> Node:
        start = self.map.start
        end = self.map.end
        open = [Node(start)]

        while open:
            cur_node = open.pop()
            if cur_node.coordinate == end:
                return cur_node

            successors = [
                Node(coordinate=s, precursor=cur_node)
                for s in self.map.get_neighbor_coordinates(cur_node.coordinate)
            ]
            open = successors + open

        print("No solution")
        return None