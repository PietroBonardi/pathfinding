import click
import yaml
from map import Map


@click.command()
@click.argument('setting_file')
def create_map(setting_file):
    setting = yaml.safe_load(open(setting_file, 'r'))
    grid = Map(setting["width"], setting["height"])
    
    for coordinate in setting["obstacles"]:
        grid.insert_element(tuple(coordinate),grid.OBSTACLE)
        
    grid.insert_element(tuple(setting["start"]), grid.START)
    grid.insert_element(tuple(setting["end"]), grid.END)


    print(grid.map)

if __name__ == "__main__":
    create_map()
