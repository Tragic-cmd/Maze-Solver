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

class MoreTests(unittest.TestCase):
    def setUp(self):
        # Create a small test maze with a fixed seed for consistent results
        self.maze = Maze(0, 0, 3, 3, 10, 10, seed=42)
    
    def test_maze_creation(self):
        # Test that maze is created with correct dimensions
        self.assertEqual(len(self.maze._cells), 3)  # num_cols
        self.assertEqual(len(self.maze._cells[0]), 3)  # num_rows
    
    def test_cells_initially_unvisited(self):
        # Test that all cells start unvisited
        for i in range(self.maze.num_cols):
            for j in range(self.maze.num_rows):
                self.assertFalse(self.maze._cells[i][j].visited)
    
    def test_entrance_and_exit(self):
        # Test entrance and exit are created correctly
        self.maze._break_entrance_and_exit()
        # Check entrance (top-left)
        self.assertFalse(self.maze._cells[0][0].has_top_wall)
        # Check exit (bottom-right)
        self.assertFalse(self.maze._cells[2][2].has_bottom_wall)
    
    def test_reset_cells_visited(self):
        # Create a small test maze
        maze = Maze(0, 0, 2, 2, 10, 10)
        # Mark some cells as visited
        maze._cells[0][0].visited = True
        maze._cells[1][1].visited = True
        # Call the reset method
        maze._reset_cells_visited()
        # Verify all cells are not visited
        for col in range(maze.num_cols):
            for row in range(maze.num_rows):
                self.assertFalse(maze._cells[col][row].visited)

if __name__ == "__main__":
    unittest.main()
