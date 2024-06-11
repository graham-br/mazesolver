from graphics import Window, Point, Line


def main():
    win = Window(800, 600)

    point1 = Point(2, 12)
    point2 = Point(200, 99)
    point3 = Point(400, 300)
    point4 = Point(700, 500)

    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    joining_line = Line(point2, point3)

    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(joining_line, "purple")

    win.wait_for_close()


main()
