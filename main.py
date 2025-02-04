from window import Window, Point, Line
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from cell import Cell
from maze import Maze

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Create a maze with visible cells (not too many to start)
    num_cols = 12
    num_rows = 10
    margin = 50
    cell_size_x = 50
    cell_size_y = 50
    
    # Create your maze
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    # Break entrance and exit
    maze._break_entrance_and_exit()

    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
