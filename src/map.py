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

        self.map = np.zeros((self.width, self.height))

    def insert_element(self, coordinate: list, label: int) -> None:
        i, j = coordinate
        assert 0 <= i <= self.width and 0 <= j <= self.height, "wrong i or j!"
        assert label in self.LABELS, "wrong label!"
        self.map[i][j] = label
