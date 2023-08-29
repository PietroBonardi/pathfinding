from pathfinder.ui.map_ui import MapUI

def main():

    map = MapUI(10,10)
    map.draw_map()
    map.window.mainloop()

if __name__ == "__main__":
    main()
