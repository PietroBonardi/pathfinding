import pytest
from pathfinder.map import Map
from pathfinder.solver import Solver
from pathfinder.shortcuts import *

grid_no_obs = Map(4, 5)
grid_obs = Map(4, 5)
grid_obs.insert_element((2, 3), OBSTACLE)

expected_0 = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
expected_1 = [(0, 1), (1, 0), (1, 1)]
expected_2 = [(2, 4), (2, 3), (3, 3)]
expected_3 = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1), (3, 2), (3, 3)]

COMBINATIONS = [(grid_no_obs, (2, 2), expected_0),
                (grid_no_obs, (0, 0), expected_1),
                (grid_no_obs, (3, 4), expected_2),
                (grid_obs, (2, 2), expected_3)]


@pytest.mark.parametrize("grid, coordinate, expected", COMBINATIONS)
def test_compact(grid, coordinate, expected):
    solver = Solver(grid)
    successors = solver.get_successors(coordinate)
    assert set(successors) == set(expected)
