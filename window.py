import tkinter


class Window:
    def __init__(self, width, height):
        self.__root = tkinter.Tk()
        self.__root.title("My Window")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = tkinter.Canvas(
            self.__root, width=width, height=height, background="black"
        )
        self.__canvas.pack(fill="both", expand=True)

        self.__running = False

    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
