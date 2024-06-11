from graphics import Point, Line


class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        if self.has_left_wall:
            self.__win.draw_line(Line(top_left, bottom_left))

        if self.has_right_wall:
            self.__win.draw_line(Line(top_right, bottom_right))

        if self.has_top_wall:
            self.__win.draw_line(Line(top_left, top_right))

        if self.has_bottom_wall:
            self.__win.draw_line(Line(bottom_left, bottom_right))