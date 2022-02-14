class Point:

    def __init__(self, x: float, y: float):
        assert isinstance(x, float), 'enter x as float'
        assert isinstance(y, float), 'enter y as float'
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f'x value: {self.__x}\ny value: {self.__y}'


if __name__ == "__main__":
    p1 = Point(100.50, 10.20)
    print(p1)
 # p1.__init__(self="",x=float(input("enter x as float: ")), y=input("enter y as float: "))
# p1.x = float(input("enter x as float: "))
# p1.y = float(input("enter y as float: "))







