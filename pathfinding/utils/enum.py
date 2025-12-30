from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CellState:
    """
    Defines the possible types of cells in a 2D grid map.

    Each cell in the map is represented by an integer value with the
    following meaning:

        - OBSTACLE (-1): Cell is blocked and cannot be traversed.
        - FREE (0): Cell is empty and can be traversed.
        - START (1): Starting position in the map.
        - END (2): Target or goal position in the map.
        - UNSET (-2): Cell has not been initialized.

    These constants are intended to be used as labels in the map matrix.
    """

    unset: int = -2
    obstacle: int = -1
    free: int = 0
    start: int = 1
    end: int = 2

    def get_states(self) -> List[int]:
        """Get all the cell states.

        Returns:
            (List): The list of all the cell states.
        """
        return [
            self.unset,
            self.obstacle,
            self.free,
            self.start,
            self.end,
        ]
