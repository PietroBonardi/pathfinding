import click
import yaml
from pathfinder.data_structure.map import Map
from pathfinder.shortcuts import *
from pathfinder.engines.search import RandomWalk


@click.command()
@click.argument('setting_file')
def main(setting_file):
    # map creation
    setting = yaml.safe_load(open(setting_file, 'r'))
    grid = Map(setting["width"], setting["height"])
    for coordinate in setting["obstacles"]:
        grid.insert_element(tuple(coordinate), OBSTACLE)

    grid.insert_element(tuple(setting["start"]), START)
    grid.insert_element(tuple(setting["end"]), END)
    print(grid.map)

    # test random walk
    random_walk = RandomWalk(grid)
    print(f"Solution:\n {random_walk.solve()}")


if __name__ == "__main__":
    main()
