import math


class GeometricObject:
    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        self.__x = float(x)
        self.__y = float(y)
        self.color = color
        self.filled = filled

    def __repr__(self):
        if self.filled is False:
            filling = 'no filled'
        else:
            filling = 'filled'

        return f'({int(self.__x)},{int(self.__y)}) {self.color} {filling}'

    def __str__(self):
        return (f'({self.__x},{self.__y})\n'
                f'color: {self.color}\n'
                f'filled: {self.filled}')

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = float(x)

    @y.setter
    def y(self, y):
        self.__y = float(y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_coordinate(self, x_value, y_value):
        self.x = x_value
        self.y = y_value

    def set_color(self, clr_value):
        self.color = clr_value

    def set_filled(self, fll_value):
        self.filled = fll_value

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled


class Circle(GeometricObject):
    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if radius < 0:
            self.__radius = 0.0
        else:
            self.__radius = float(radius)


    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, rds_value):
        if rds_value > 0:
            self.__radius = float(rds_value)

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimetr(self):
        return math.pi * self.__radius * 2

    def get_diametr(self):
        return self.__radius * 2

    def __repr__(self):
        if self.filled is False:
            filling = 'no filled'
        else:
            filling = 'filled'

        return f'radius:{int(self.__radius)} ({int(self.x)},{int(self.y)}) {self.color} {filling}'

    def __str__(self):
        return (f'radius: {self.__radius}\n'
                f'({self.x},{self.y})\n'
                f'color: {self.color}\n'
                f'filled: {self.filled}')


class Rectangle(GeometricObject):
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if width < 0:
            self.width = 0.0
        else:
            self.width = float(width)
        if height < 0:
            self.height = 0.0
        else:
            self.height = float(height)

    def set_width(self, w_value):
        if w_value > 0:
            self.width = float(w_value)

    def set_height(self, h_value):
        if h_value > 0:
            self.height = float(h_value)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return self.width * 2 + self.height * 2

    def __repr__(self):
        if self.filled is False:
            filling = 'no filled'
        else:
            filling = 'filled'

        return f'width:{int(self.width)} height:{int(self.height)} ({int(self.x)},{int(self.y)}) {self.color} {filling}'

    def __str__(self):
        return (f'width: {self.width}\n'
                f'height: {self.height}\n'
                f'({self.x},{self.y})\n'
                f'color: {self.color}\n'
                f'filled: {self.filled}')


point = GeometricObject()
print(point)
print()
point.set_coordinate(-4, 9)
print(point.get_x())
print(point.get_y())
point.set_color('red')
print(point.get_color())
point.set_filled(True)
print(point.is_filled())
print()
print(point)
print()
point_2 = GeometricObject(8, -4, 'blue', True)
print(point_2)
print()
circle = Circle()
print(circle)
print()
circle.radius = -34
print(circle.radius)
circle.radius = 12
print(circle.radius)
print()
circle_2 = Circle(3, -100, 20, 'green', True)
print(circle_2)
print()
circle_2.set_color('grey')
print(circle_2.get_color())
print()
print(circle_2.get_area())
print(circle_2.get_perimetr())
print(circle_2.get_diametr())
print()
circle_3 = Circle(90, -84, -223, 'pink')
print(circle_3)
print()
rectangle = Rectangle()
print(rectangle)
print()
rectangle.set_coordinate(11, 29)
rectangle.set_color('yellow')
rectangle.set_width(-10)
rectangle.set_height(20)
print(rectangle)
print()
rectangle.set_width(100)
print(rectangle.get_width())
print(rectangle.get_height())
print()
print(rectangle.get_area())
print(rectangle.get_perimetr())
print()
rectangle_2 = Rectangle(10, 20, 30, -40, 'brown', True)
print(rectangle_2)
print()
figures = []
figures.append(point)
figures.append(circle_2)
figures.append(rectangle)
print(figures)
