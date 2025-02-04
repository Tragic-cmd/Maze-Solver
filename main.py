from window import Window, Point, Line
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from cell import Cell
from maze import Maze

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    maze = Maze(10, 10, 10, 10, 40, 40, win)
    
    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
