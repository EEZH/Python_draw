import turtle


class Figure:
    pen = turtle.Pen()


    def __init__(self, color="black", width=1, angle=60, size=100):
        self.pen.color(color)
        self.pen.width(width)
        self.angle = angle
        self.size = size

    def render(self, itters, is_right=True):
        itters = range(itters)
        turn = self.pen.right if is_right else self.pen.left
        for i in itters:
            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()
        
class Dynamic_figure(Figure):
    def __init__(self, color, width, angle, size, diff=1):
        super().__init__(color, width, angle, size)
        self.diff = diff

    def render(self, itters, is_right=True):
        itters = range(itters)
        turn = self.pen.right if is_right else self.pen.left
        for i in itters:
            self.size -= self.diff

            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()


class Colorful_figure(Figure):
    def __init__(self, color, width, angle, size, colors=None):
        super().__init__(color, width, angle, size)
        self.colors = colors if colors else []

    def render(self, itters, is_right=True):
        itters = range(itters)
        colors_count = len(self.colors)
        turn = self.pen.right if is_right else self.pen.left
        for i in itters:
            cur_color = self.colors[i % colors_count]
            self.pen.color(cur_color)
            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()

class DynCol_Figure(Dynamic_figure,Colorful_figure):
    def __init__(self, color, width, angle, size, colors, diff):
        Dynamic_figure.__init__(self, color, width, angle, size, diff)
        Colorful_figure.__init__(self, color, width, angle, size, colors)

    def render(self, itters, is_right=True):
        itters = range(itters)
        colors_count = len(self.colors)
        turn = self.pen.right if is_right else self.pen.left
        for i in itters:
            cur_color = self.colors[i % colors_count]
            self.pen.color(cur_color)
            self.size -= self.diff
            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()
