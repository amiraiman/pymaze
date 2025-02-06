from time import sleep
from graphics import Line, Point
import random


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._win = win
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black"
            )

        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black"
            )

        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black"
            )

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black"
            )

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        color = "red" if undo else "gray"
        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        end_x = (to_cell._x1 + to_cell._x2) // 2
        end_y = (to_cell._y1 + to_cell._y2) // 2

        self._win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), color)


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, size_x, size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._size_x = size_x
        self._size_y = size_y
        self._win = win
        self._cells = []

        self._create_cells()
        if seed is not None:
            random.seed(seed)
        if self._num_cols != 0 and self._num_rows != 0:
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        start_x = self._x1 + i * self._size_x
        start_y = self._y1 + j * self._size_y
        self._cells[i][j].draw(
            start_x,
            start_y,
            start_x + self._size_x,
            start_y + self._size_y,
        )
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        sleep(0.005)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]

        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        print(f"Visiting cell ({i}, {j})")
        current = self._cells[i][j]
        current.visited = True

        while True:
            possible_moves_points = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ]
            possible_moves = []

            for x, y in possible_moves_points:
                if 0 <= x < self._num_cols and 0 <= y < self._num_rows:
                    if not self._cells[x][y].visited:
                        possible_moves.append((x, y))

            if len(possible_moves) == 0:
                print(f"No move from cell ({i}, {j}). Exiting.")
                self._draw_cell(i, j)
                return

            print(f"Possible moves from cell ({i}, {j}) {possible_moves}")
            chosen_i, chosen_j = random.choice(possible_moves)
            chosen = self._cells[chosen_i][chosen_j]
            print(f"Move from ({i}, {j}) to ({chosen_i}, {chosen_j}).")

            if chosen_i == (i - 1):
                current.has_left_wall = False
                chosen.has_right_wall = False

            if chosen_i == (i + 1):
                current.has_right_wall = False
                chosen.has_left_wall = False

            if chosen_j == (j + 1):
                current.has_bottom_wall = False
                chosen.has_top_wall = False

            if chosen_j == (j - 1):
                current.has_top_wall = False
                chosen.has_bottom_wall = False

            self._break_walls_r(chosen_i, chosen_j)
