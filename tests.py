import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2 = Maze(0, 0, num_cols, num_rows, 10, 10)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        self.assertEqual(len(m2._cells), num_rows)
        self.assertEqual(len(m2._cells[0]), num_cols)

    def test_maze_create_empty_cols(self):
        start_x = 100
        start_y = 1000
        size_x = 100
        size_y = 100

        num_cols = 0
        num_rows = 0
        m1 = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y)
        m2 = Maze(start_x, start_y, num_rows + 1, num_cols, size_x, size_y)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m2._cells), num_cols)

    def test_maze_create_empty_rows(self):
        start_x = 100
        start_y = 1000
        size_x = 100
        size_y = 100

        num_cols = 10
        num_rows = 0
        m1 = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_entrance_and_exit(self):
        start_x = 100
        start_y = 1000
        size_x = 100
        size_y = 100

        num_cols = 10
        num_rows = 10
        m1 = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_maze_entrance_and_exit_empty_grid(self):
        start_x = 100
        start_y = 1000
        size_x = 100
        size_y = 100

        num_cols = 0
        num_rows = 0
        m1 = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y)
        self.assertEqual(len(m1._cells), 0)


if __name__ == "__main__":
    unittest.main()
