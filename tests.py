import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_min_size(self):
        num_cols = 1
        num_rows = 1
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_cell_walls(self):
        num_cols = 3
        num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        cell = maze._cells[0][0]  # Top-left corner cell
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_left_wall)

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze._break_entrance_and_exit()
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_rows-1][num_cols-1].has_bottom_wall)

    def test_maze_creation_and_entrance_exit(self):
        # Create a small test maze (e.g., 3x3)
        num_rows = 3
        num_cols = 3
        cell_size_x = 10
        cell_size_y = 10
        test_maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, win=None)
        
        # Test if maze was created with correct dimensions
        self.assertEqual(len(test_maze._cells), num_cols, "Wrong number of columns")
        self.assertEqual(len(test_maze._cells[0]), num_rows, "Wrong number of rows")
        
        # Test initial state (all walls should exist)
        self.assertTrue(test_maze._cells[0][0].has_top_wall, "Top wall should exist initially")
        self.assertTrue(test_maze._cells[num_rows-1][num_cols-1].has_bottom_wall, "Bottom wall should exist initially")
        
        # Break entrance and exit
        test_maze._break_entrance_and_exit()
        
        # Test if entrance (top-left) and exit (bottom-right) walls are broken
        self.assertFalse(test_maze._cells[0][0].has_top_wall, "Entrance (top) wall should be broken")
        self.assertFalse(test_maze._cells[num_rows-1][num_cols-1].has_bottom_wall, "Exit (bottom) wall should be broken")



if __name__ == "__main__":
    unittest.main()
