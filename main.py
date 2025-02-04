from graphics import Point, Line, Window
from maze import Cell, Maze


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
    for i in range(10):
        cell = Cell(win)

        if i == 9:
            cell.has_bottom_wall = False
            cell.has_left_wall = False
        elif prev_cell:
            cell.has_left_wall = False
            cell.has_right_wall = False
        else:
            cell.has_right_wall = False

        cell.draw(row_x1, row_y1, row_x1 + cell_width, row_y1 + cell_width)
        if prev_cell:
            prev_cell.draw_move(cell)

        prev_cell = cell
        row_x1 += cell_width

    row_y1 += cell_width
    row_x1 -= cell_width
    for i in range(10):
        cell = Cell(win)

        if i == 0:
            cell.has_top_wall = False
            cell.has_right_wall = False
        elif i == 9:
            cell.has_bottom_wall = False
            cell.has_left_wall = False
        elif prev_cell:
            cell.has_left_wall = False
            cell.has_right_wall = False

        cell.draw(row_x1, row_y1, row_x1 + cell_width, row_y1 + cell_width)
        if prev_cell:
            prev_cell.draw_move(cell, True)

        prev_cell = cell
        row_x1 += cell_width


def main():
    win = Window(800, 600)
    print_start_arrow(win, "red")
    # print_maze(win, 60, 60)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    win.wait_for_close()


def maze():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()


if __name__ == "__main__":
    maze()
