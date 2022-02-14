import math


class Circle:

    def __init__(self, radius: float = 1.0, color: str = "red"):
        self.__radius = radius
        self.__color = color

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        assert isinstance(new_radius, float), 'new radius must be float'
        if new_radius <= 0:
            raise ValueError
        self.__radius = new_radius

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        assert isinstance(new_color, str), 'new color must be string '
        self.__color = new_color

    def get_area(self):
        area = round(self.__radius * self.__radius * math.pi, 2)
        return area

    def get_circumference(self):
        circumference = round(((self.__radius * 2)*math.pi), 2)
        return circumference

    def __str__(self):
        return f'radius is : {self.__radius} \ncolor is : {self.__color}'


c1 = Circle(15)
print(c1)
