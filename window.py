from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("aMazeing Auto Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill="both", expand=True)
        self.__running = False  # Tracks if the window is "running"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Call close() when user closes the window

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True  # The window is now "running"
        while self.__running:  # Keep the app running until it's closed
            self.redraw()      # Redraw the window

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def draw_rectangle(self, x1, y1, x2, y2, color="white"):
        """Draw a rectangle on the canvas."""
        self.__canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2
        )
