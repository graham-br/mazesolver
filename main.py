from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(10, 10, 20, 20, win)
    cell1.has_right_wall = False
    cell1.has_bottom_wall = False
    cell2 = Cell(20, 10, 30, 20, win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3 = Cell(20, 20, 30, 30, win)
    cell3.has_top_wall = False
    cell3.has_left_wall = False
    cell4 = Cell(10, 20, 20, 30, win)
    cell4.has_top_wall = False
    cell4.has_right_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)
    cell4.draw_move(cell1)
    cell1.draw_move(cell4, undo=True)

    win.wait_for_close()


main()
