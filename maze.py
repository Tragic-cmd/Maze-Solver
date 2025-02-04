import time
import random
from cell import Cell
from window import Window

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        # create the columns
        for i in range(0, self.num_cols):
            col = []
            for j in range(0, self.num_rows):
                x1 = self._x1 + (i * self.cell_size_x)
                y1 = self._y1 + (j * self.cell_size_y)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, y1, x2, y2, self.win)
                col.append(cell)
            self._cells.append(col)
        # draw all cells after the grid is created
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # Break entrance (top wall of top-left cell)
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        # Break exit (bottom wall of bottom-right cell)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            unvisited = []
            if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
                unvisited.append((i, j+1))
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                unvisited.append((i, j-1))
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                unvisited.append((i+1, j))
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                unvisited.append((i-1, j))
            if not unvisited:
                return
            rand_index = random.randrange(len(unvisited))
            next_i, next_j = unvisited[rand_index]
            if next_j > j: # moving down
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_top_wall = False
                self._draw_cell(next_i, next_j)
            if next_j < j: # moving up
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_bottom_wall = False
                self._draw_cell(next_i, next_j)
            if next_i > i:  # moving right
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_left_wall = False
                self._draw_cell(next_i, next_j)
            if next_i < i: # moving left
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_right_wall = False
                self._draw_cell(next_i, next_j)
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                item = self._cells[col][row]
                item.visited = False

    def generate_maze(self):
        self._break_walls_r(0, 0)
        self._break_entrance_and_exit()
        self._reset_cells_visited()
        self.solve()

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        # Check if we can move right
        if (i + 1 < self.num_cols and  # within bounds
            not self._cells[i][j].has_right_wall and  # no wall blocking
            not self._cells[i + 1][j].visited):  # haven't been there
            # Draw move to the right
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            # Recursively try this path
            if self._solve_r(i + 1, j):
                return True
            # If we get here, this path failed
            # Undo the move
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # Check if we can move left
        if (i - 1 >= 0 and  # within bounds
            not self._cells[i][j].has_left_wall and  # no wall blocking
            not self._cells[i - 1][j].visited):  # haven't been there
            # Draw move to the left
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            # Recursively try this path
            if self._solve_r(i - 1, j):
                return True
            # If we get here, this path failed
            # Undo the move
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # Check if we can move down
        if (j + 1 < self.num_rows and  # within bounds
            not self._cells[i][j].has_bottom_wall and  # no wall blocking
            not self._cells[i][j + 1].visited):  # haven't been there
            # Draw move down
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            # Recursively try this path
            if self._solve_r(i, j + 1):
                return True
            # If we get here, this path failed
            # Undo the move
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # Check if we can move up
        if (j - 1 >= 0 and  # within bounds
            not self._cells[i][j].has_top_wall and  # no wall blocking
            not self._cells[i][j - 1].visited):  # haven't been there
            # Draw move to the up
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            # Recursively try this path
            if self._solve_r(i, j - 1):
                return True
            # If we get here, this path failed
            # Undo the move
            self._cells[i][j].draw_move(self._cells[i][j - 1], True) 

        # The maze could not be solved
        return False




