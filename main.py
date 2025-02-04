from window import Window, Point, Line
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from cell import Cell
from maze import Maze

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Calculate maze dimensions
    margin = 50
    num_cols = 12
    num_rows = 10
    cell_size_x = (SCREEN_WIDTH - 2 * margin) // num_cols
    cell_size_y = (SCREEN_HEIGHT - 2 * margin) // num_rows
    
    # Create maze with optional seed for debugging
    maze = Maze(
        x1=margin,
        y1=margin,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=cell_size_x,
        cell_size_y=cell_size_y,
        win=win,
        seed=None  # Set to a number like 0 for debugging
    )
    
    # Generate the maze
    maze.generate_maze()

    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
