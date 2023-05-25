import pytest
from pathfinder.map import Map
from pathfinder.solver import Solver


def test_get_successors():
    grid = Map(4, 5)

    solver = Solver(grid)

    successors = solver.get_successors((2, 2))
    assert len(successors) == 8

    successors = solver.get_successors((0, 0))
    assert len(successors) == 3
    assert set(successors) == set([(0, 1), (1, 0), (1, 1)])

    successors = solver.get_successors((3, 4))
    assert len(successors) == 3
    assert set(successors) == set([(2, 4), (2, 3), (3, 3)])

    # using obstacles
    grid.insert_element((2, 3),grid.OBSTACLE)
    successors = solver.get_successors((2, 2))
    assert len(successors) == 7
    assert set(successors) == set(
        [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1), (3, 2), (3, 3)])
