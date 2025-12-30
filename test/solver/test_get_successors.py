import pytest
from pathfinding.data_structure.map import Map
from pathfinding.utils.shortcuts import CELL_STATES

map_no_obs = Map(rows=4, cols=5)
map_obs = Map(rows=4, cols=5)
map_obs.insert_element(coordinate=(2, 3), label=CELL_STATES.obstacle)

expected_0 = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
expected_1 = [(0, 1), (1, 0), (1, 1)]
expected_2 = [(2, 4), (2, 3), (3, 3)]
expected_3 = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1), (3, 2), (3, 3)]

COMBINATIONS = [
    (map_no_obs, (2, 2), expected_0),
    (map_no_obs, (0, 0), expected_1),
    (map_no_obs, (3, 4), expected_2),
    (map_obs, (2, 2), expected_3),
]


@pytest.mark.parametrize("map, coordinate, expected", COMBINATIONS)
def test_get_neighbor_coordinates(map, coordinate, expected):
    coordinates = map.get_neighbor_coordinates(coordinate)
    assert set(coordinates) == set(expected)
