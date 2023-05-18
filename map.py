import numpy as np
import click 
import yaml

OBSTACLE = -1
START = 1
END = 2
FREE = 0
LABELS = set([OBSTACLE, START, END, FREE])

class Map():

    def __init__(self, width: int, height: int) -> None:
        assert width >=0 and height>=0
        self.width = width
        self.height = height
        
        self.map = np.zeros((self.width, self.height))

    def insert_element(self, coordinates:tuple, label:int) -> None:
        (i,j) = coordinates

        assert 0 <= i <= self.width and 0 <= j <= self.height, "wrong i or j!"
        assert label in LABELS, "wrong label!"
        self.map[i][j] = label


@click.command()
@click.argument('setting_file')
def create_map(setting_file):    
    setting = yaml.safe_load(open(setting_file, 'r'))
    grid = Map(setting["width"], setting["height"])
    map(lambda x: grid.insert_element(x,OBSTACLE), setting["obstacles"])
    
    grid.insert_element(tuple(setting["start"]),START)
    grid.insert_element(tuple(setting["end"]),END)

    print(grid.map)
    
    




    

    

if __name__ == "__main__":
    create_map()
