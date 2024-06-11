import time
import random

from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        random_seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        random.seed(random_seed)

        self.__create_cells()
        self.__break_entrance_and_exit()

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
            self._cells.append(new_row_list)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self._cells[i][j].draw()
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.025)

    def __break_entrance_and_exit(self):
        if random.randint(0, 1) == 0:
            self._cells[0][0].has_right_wall = False
        else:
            self._cells[0][0].has_bottom_wall = False
        self.__draw_cell(0, 0)
        if random.randint(0, 1) == 0:
            self._cells[self.__num_cols - 1][self.__num_rows - 1].has_left_wall = False
        else:
            self._cells[self.__num_cols - 1][self.__num_rows - 1].has_top_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
