import time

from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.__create_cells()

    def __create_cells(self):
        for col in range(self.__num_cols):
            x1 = self.__x1 + (col * self.__cell_size_x)
            x2 = x1 + self.__cell_size_x
            new_row_list = []
            for row in range(self.__num_rows):
                y1 = self.__y1 + (row * self.__cell_size_y)
                y2 = y1 + self.__cell_size_y
                new_cell = Cell(x1, y1, x2, y2, self.__win)
                new_row_list.append(new_cell)
            self.__cells.append(new_row_list)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.025)
