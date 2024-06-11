from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(10, 10, 20, 20, win)
    cell2 = Cell(30, 30, 40, 40, win)
    cell2.has_bottom_wall = False
    cell3 = Cell(50, 50, 60, 60, win)
    cell3.has_bottom_wall = False
    cell3.has_top_wall = False
    cell4 = Cell(70, 70, 80, 80, win)
    cell4.has_right_wall = False
    cell4.has_left_wall = False
    cell5 = Cell(90, 90, 100, 100, win)
    cell5.has_top_wall = False
    cell5.has_left_wall = False
    cell5.has_right_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()

    win.wait_for_close()


main()
