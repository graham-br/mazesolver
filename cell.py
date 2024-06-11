from graphics import Point, Line

remove_color = "white"


class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
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
        if self.__win is None:
            return
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        if self.has_left_wall:
            self.__win.draw_line(Line(top_left, bottom_left))
        else:
            self.__win.draw_line(Line(top_left, bottom_left), remove_color)

        if self.has_right_wall:
            self.__win.draw_line(Line(top_right, bottom_right))
        else:
            self.__win.draw_line(Line(top_right, bottom_right), remove_color)

        if self.has_top_wall:
            self.__win.draw_line(Line(top_left, top_right))
        else:
            self.__win.draw_line(Line(top_left, top_right), remove_color)
        if self.has_bottom_wall:
            self.__win.draw_line(Line(bottom_left, bottom_right))
        else:
            self.__win.draw_line(Line(bottom_left, bottom_right), remove_color)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"

        source_center = Point(
            (self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2
        )
        dest_center = Point(
            (to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2
        )
        line = Line(source_center, dest_center)

        self.__win.draw_line(line, line_color)
