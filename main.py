from pathfinder.data_structure.map import Map
from pathfinder.ui.map_ui import MapUI


def main():
    map_ui = MapUI(5, 5)
    map_ui.create_map()
    map_ui.window.mainloop()
    

if __name__ == "__main__":
    main()
