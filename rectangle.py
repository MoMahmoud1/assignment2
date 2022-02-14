from point import Point
from line import Line


class Rectangle:

    def __init__(self, bottom_left_corner: Point, top_right_corner: Point):
        self.__bottom_left_corner = bottom_left_corner
        self.__top_right_corner = top_right_corner

    @property
    def bottom_left_corner(self):
        return self.__bottom_left_corner

    @property
    def top_right_corner(self):
        return self.__top_right_corner

    @property
    def bottom_right_corner(self):
        new_point_object = Point(self.bottom_left_corner.y, self.top_right_corner.x)
        return new_point_object

    def left_corner(self):
        point_object = Point(self.bottom_left_corner.y, self.bottom_left_corner.x)
        return point_object

    def bottom_right(self):
        bottom_right_object = Point(self.__bottom_left_corner.y, self.__top_right_corner.x)
        return bottom_right_object

    def area(self):
        line_1 = Line(Point(self.__bottom_left_corner.x, self.__bottom_left_corner.y),
                      Point(self.left_corner().x, self.left_corner().y))
        line_2 = Line(Point(self.bottom_right().x, self.bottom_right().y),
                      Point(self.__top_right_corner.x, self.__top_right_corner.y))
        rectangle_length = line_1.length()
        rectangle_width = line_2.length()

        area = round(rectangle_length * rectangle_width, 2)
        return area

    def perimeter(self):
        line_3 = Line(Point(self.__bottom_left_corner.x, self.__bottom_left_corner.y),
                      Point(self.left_corner().x, self.left_corner().y))
        line_4 = Line(Point(self.bottom_right().x, self.bottom_right().y),
                      Point(self.__top_right_corner.x, self.__top_right_corner.y))
        rectangle_length = line_3.length()
        rectangle_width = line_4.length()
        perimeter = round((rectangle_length * 2) + (rectangle_width * 2), 2)
        return perimeter
