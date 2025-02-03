from window import Window, Point, Line
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from cell import Cell

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create cells in a 2x3 grid pattern
    # Top row
    cell1 = Cell(50, 50, 150, 150, win)
    cell2 = Cell(150, 50, 250, 150, win)
    cell3 = Cell(250, 50, 350, 150, win)

    # Bottom row
    cell4 = Cell(50, 150, 150, 250, win)
    cell5 = Cell(150, 150, 250, 250, win)
    cell6 = Cell(250, 150, 350, 250, win)

    # Create an interesting pattern by removing some walls
    cell1.has_right_wall = False
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell3.has_left_wall = False
    cell4.has_top_wall = False
    cell4.has_right_wall = False
    cell5.has_left_wall = False
    cell5.has_right_wall = False
    cell6.has_left_wall = False
    cell3.has_bottom_wall = False
    cell6.has_top_wall = False
    # Try removing some more walls!

    # Draw all cells
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()
    cell6.draw()
    
    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
