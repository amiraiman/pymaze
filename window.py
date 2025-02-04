import tkinter


class Window:
    def __init__(self, width, height):
        self.__root = tkinter.Tk()
        self.__root.title("My Window")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__running = False

    def run(self):
        self.__running = True
        self.__root.mainloop()

        while self.__running:
            self.__root.update()

    def close(self):
        self.__running = False
        self.__root.destroy()
