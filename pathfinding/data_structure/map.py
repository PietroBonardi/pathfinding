import numpy as np
from typing import Tuple, List
from pathfinding.utils.shortcuts import CELL_STATES


class Map:
    """
    Represents a 2D grid map implemented as a matrix of size (rows x cols).

    Each cell of the map contains an integer label with the following meaning:
        - UNSET = -2
        - OBSTACLE = -1
        - FREE     = 0
        - START    = 1
        - END      = 2

    The map is internally stored as a NumPy 2D array.
    """
    def __init__(self, rows: int, cols: int):
        """
        Initialize a Map with the given number of rows and columns.

        All cells are initialized as FREE (0). The start and end positions
        are initially unset.

        Args:
            rows (int): Number of rows of the map. Must be greater than 0.
            cols (int): Number of columns of the map. Must be greater than 0.

        Raises:
            ValueError: If rows or cols are less than or equal to 0.
        """
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows/Columns number has to be greater than 0.")
        self.rows = rows
        self.cols = cols
        self.start = CELL_STATES.unset
        self.end = CELL_STATES.unset
        # set each element to "FREE (= 0)" 
        self.map = np.zeros((self.rows, self.cols))

    def is_inside(self, coordinate: Tuple[int, int]) -> bool:
        """
        Check whether a coordinate lies inside the map boundaries.

        Args:
            coordinate (Tuple[int, int]): A tuple (row, column) representing
                the position to check.

        Returns:
            bool: True if the coordinate is inside the map, False otherwise.
        """
        i, j = coordinate
        return 0 <= i < self.rows and 0 <= j < self.cols

    def get_element(self, coordinate: Tuple[int, int]) -> int:
        """
        Retrieve the value stored at a given coordinate.

        Args:
            coordinate (Tuple[int, int]): A tuple (row, column) representing
                the position to access.

        Raises:
            ValueError: If the coordinate is outside the map.

        Returns:
            int: The label stored at the given coordinate.
        """
        if not self.is_inside(coordinate):
            raise ValueError("Wrong coordinate.")
        i, j = coordinate
        return self.map[i, j]

    def insert_element(self, coordinate: Tuple[int, int], label: int) -> None:
        """
        Insert a label into the map at the specified coordinate.

        If the label corresponds to START or END, the respective attribute
        is updated with the given coordinate.

        Args:
            coordinate (Tuple[int, int]): A tuple (row, column) representing
                where to insert the label.
            label (int): The label to insert. Must be one of the allowed labels.

        Raises:
            ValueError: If the coordinate is outside the map.
            ValueError: If the label is not valid.
        """
        if not self.is_inside(coordinate):
            raise ValueError("Wrong coordinate.")
        if label not in CELL_STATES.get_states():
            raise ValueError("Wrong label.")
        i, j = coordinate 
        self.map[i][j] = label
        # init start and end coordinate 
        if label == CELL_STATES.start:
            self.start = coordinate
        elif label == CELL_STATES.end:
            self.end = coordinate

    def get_neighbor_coordinates(self, coordinates: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Return all valid successor coordinates of a given cell.

        A successor is any neighboring cell (including diagonals) that:
            - lies within the map boundaries
            - is not the same as the input cell
            - is not an obstacle

        Args:
            coordinates (Tuple[int, int]): A tuple (row, column) representing
                the reference cell.

        Returns:
            List[Tuple[int, int]]: A list of coordinates corresponding to
            all valid neighboring cells.
        """
        i, j = coordinates
        coordinates = []
        lower_i = max(i - 1, 0)
        upper_i = min(i + 1, self.rows - 1)
        lower_j = max(j - 1, 0)
        upper_j = min(j + 1, self.cols - 1)

        for next_i in range(lower_i, upper_i + 1):
            for next_j in range(lower_j, upper_j + 1):
                if not (next_i == i and next_j == j):
                    if self.get_element((next_i, next_j)) != CELL_STATES.obstacle:
                        coordinates.append((next_i, next_j))

        return coordinates