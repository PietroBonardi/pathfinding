import numpy as np


class Map():
    OBSTACLE = -1
    START = 1
    END = 2
    FREE = 0
    LABELS = set([OBSTACLE, START, END, FREE])

    def __init__(self, width: int, height: int) -> None:
        assert width >= 0 and height >= 0
        self.width = width
        self.height = height

        self.start = None
        self.end = None

        self.map = np.zeros((self.width, self.height))

    def check_coordinate(self, coordinate: list) -> bool:
        i, j = coordinate
        assert 0 <= i <= self.width and 0 <= j <= self.height, "wrong i or j!"

    def insert_element(self, coordinate: list, label: int) -> None:
        i, j = coordinate
        self.check_coordinate(coordinate)
        assert label in self.LABELS, "wrong label!"
        self.map[i][j] = label
        if label == self.START:
            self.start = coordinate
        elif label == self.END:
            self.end = coordinate

    def get_successors(self, coordinate: list):
        pass
