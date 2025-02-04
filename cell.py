from window import Line, Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win:
            if self.has_left_wall:
                point1 = Point(self._x1, self._y1)
                point2 = Point(self._x1, self._y2)
                line = Line(point1, point2)
                self._win.draw_line(line, "black")
            else:
                # Draw a "removed" wall in background color
                point1 = Point(self._x1, self._y1)
                point2 = Point(self._x1, self._y2)
                line = Line(point1, point2)
                self._win.draw_line(line, "#d9d9d9")
            if self.has_right_wall:
                point1 = Point(self._x2, self._y1)
                point2 = Point(self._x2, self._y2)
                line = Line(point1, point2)
                self._win.draw_line(line, "black")
            else:
                # Draw a "removed" wall in background color
                point1 = Point(self._x2, self._y1)
                point2 = Point(self._x2, self._y2)
                line = Line(point1, point2)
                self._win.draw_line(line, "#d9d9d9")
            if self.has_top_wall:
                point1 = Point(self._x1, self._y1)
                point2 = Point(self._x2, self._y1)
                line = Line(point1, point2)
                self._win.draw_line(line, "black")
            else:
                # Draw a "removed" wall in background color
                point1 = Point(self._x1, self._y1)
                point2 = Point(self._x2, self._y1)
                line = Line(point1, point2)
                self._win.draw_line(line, "#d9d9d9")
            if self.has_bottom_wall:
                point1 = Point(self._x1, self._y2)
                point2 = Point(self._x2, self._y2)
                line = Line(point1, point2)
                self._win.draw_line(line, "black")
            else:
                # Draw a "removed" wall in background color
                point1 = Point(self._x1, self._y2)
                point2 = Point(self._x2, self._y2)
                line = Line(point1, point2)
                self._win.draw_line(line, "#d9d9d9")        

    def draw_move(self, to_cell, undo=False):
        self_x1 = (self._x1 + self._x2) / 2
        self_y1 = (self._y1 + self._y2) / 2
        point1 = Point(self_x1, self_y1)
        to_cell_x1 = (to_cell._x1 + to_cell._x2) / 2
        to_cell_y1 = (to_cell._y1 + to_cell._y2) / 2
        point2 = Point(to_cell_x1, to_cell_y1)
        line = Line(point1, point2)
        color = "red" if not undo else "gray"
        self._win.draw_line(line, color)  # Try passing color to draw_line