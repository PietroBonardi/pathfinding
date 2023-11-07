import numpy as np
from typing import Tuple
from pathfinder.shortcuts import *

class Map():

    def __init__(self, row: int, col: int) -> None:
        assert row >= 0 and col >= 0
        self.row = row
        self.col = col
        self.start = None
        self.end = None
        self.map = np.zeros((self.row, self.col))

    def is_inside(self, coordinate: Tuple[int,int]) -> bool:
        i, j = coordinate
        return 0 <= i < self.row and 0 <= j < self.col
    
    def get_element(self, coordinate: Tuple[int,int]):
        assert self.is_inside(coordinate), "wrong coordinate!"
        i, j = coordinate
        return self.map[i, j]

    def insert_element(self, coordinate: Tuple[int,int], label: int) -> None:
        i, j = coordinate
        assert self.is_inside(coordinate), "wrong coordinate!"
        assert label in LABELS, "wrong label!"
        self.map[i][j] = label

        if label == START:
            self.start = coordinate
        elif label == END:
            self.end = coordinate
    
    def get_successors(self, coordinates: Tuple[int, int]) -> list[int]:
        i, j = coordinates
        successor = []
        lower_i = max(i-1, 0)
        upper_i = min(i+1, self.row-1)
        lower_j = max(j-1, 0)
        upper_j = min(j+1, self.col-1)
        
        for next_i in range(lower_i, upper_i+1):
            for next_j in range(lower_j, upper_j+1):
                if not (next_i == i and next_j == j):
                    if self.get_element((next_i, next_j)) != OBSTACLE:
                        successor.append((next_i, next_j))

        return successor

            