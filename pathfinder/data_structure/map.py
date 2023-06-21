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

            