from time import sleep
from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._win = win
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white"
            )

        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white"
            )

        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white"
            )

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white"
            )

    def draw_move(self, to_cell, undo=False):
        color = "red" if undo else "gray"
        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        end_x = (to_cell._x1 + to_cell._x2) // 2
        end_y = (to_cell._y1 + to_cell._y2) // 2

        self._win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), color)


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, size_x, size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._size_x = size_x
        self._size_y = size_y
        self._win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            rows = []
            for j in range(self._num_cols):
                rows.append(self._draw_cells(i, j))
            self._cells.append(rows)

    def _draw_cells(self, i, j):
        cell = Cell(self._win)
        start_x = self._x1 + j * self._size_x
        start_y = self._y1 + i * self._size_y

        cell.draw(
            start_x,
            start_y,
            start_x + self._size_x,
            start_y + self._size_y,
        )
        # cell.draw(
        #     self._x1 + j * self._size_x,
        #     self._y1 + i * self._size_y,
        #     self._x1 + (j + 1) * self._size_x,
        #     self._y1 + (i + 1) * self._size_y,
        # )

        self._animate()
        return cell

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
