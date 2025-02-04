from window import Window
from graphics import Point, Line

p1 = Point(20, 20)
p2 = Point(50, 50)
ln = Line(p1, p2, "blue")

win = Window(800, 600)
win.draw_line(ln)
win.run()
