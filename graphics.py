class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2, color="white", size=2):
        self.__p1 = p1
        self.__p2 = p2
        self.__color = color
        self.__size = size

    def draw(self, canvas):
        canvas.create_line(
            self.__p1.x,
            self.__p1.y,
            self.__p2.x,
            self.__p2.y,
            fill=self.__color,
            width=self.__size,
        )
