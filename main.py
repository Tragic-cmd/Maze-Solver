from window import Window, Point, Line
from constants import *

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Create points
    p1 = Point(100, 200)  # bottom left
    p2 = Point(200, 200)  # bottom right
    p3 = Point(150, 100)  # top of roof

    # Create some lines
    line1 = Line(p1, p2)
    line2 = Line(p1, p3)

    # Draw with different colors
    win.draw_line(line1, "blue")
    win.draw_line(line2, "red")
    
    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
