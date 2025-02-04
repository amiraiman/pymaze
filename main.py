from window import Window
from graphics import Point, Line, Cell


def print_start_arrow(win, color):
    head_height = 5
    line = Line(Point(20, 20), Point(50, 50))
    head_top = Line(Point(50, 50), Point(50 - head_height / 0.5, 50 - head_height / 2))
    head_bottom = Line(
        Point(50, 50), Point(50 - head_height / 2, 50 - head_height / 0.5)
    )

    win.draw_line(line, color)
    win.draw_line(head_top, color)
    win.draw_line(head_bottom, color)


def print_maze(win, start_x1, start_y1):
    cell_width = 30
    row_x1 = start_x1
    row_y1 = start_y1
    prev_cell = None
    for _ in range(10):
        cell = Cell(win)
        if prev_cell:
            cell.has_left_wall = False
            cell.has_right_wall = False
        else:
            cell.has_right_wall = False

        cell.draw(row_x1, row_y1, row_x1 + cell_width, row_y1 + cell_width)
        row_x1 += cell_width
        prev_cell = cell


win = Window(800, 600)
print_start_arrow(win, "red")
print_maze(win, 60, 60)
win.run()
