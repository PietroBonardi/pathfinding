import click
import yaml
from map import Map


@click.command()
@click.argument('setting_file')
def create_map(setting_file):
    setting = yaml.safe_load(open(setting_file, 'r'))
    grid = Map(setting["width"], setting["height"])
    
    # lazy eval
    # list(map(lambda coordinate:grid.insert_element(coordinate,grid.OBSTACLE),setting["obstacles"]))
    for coordinate in setting["obstacles"]:
        grid.insert_element(coordinate,grid.OBSTACLE)
        
    grid.insert_element(setting["start"], grid.START)
    grid.insert_element(setting["end"], grid.END)


    print(grid.map)

if __name__ == "__main__":
    create_map()
