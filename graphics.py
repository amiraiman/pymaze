class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas, color, size=2):
        canvas.create_line(
            self._p1.x,
            self._p1.y,
            self._p2.x,
            self._p2.y,
            fill=color,
            width=size,
        )
