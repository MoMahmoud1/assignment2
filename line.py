from point import Point
import math


class Line:

    def __init__(self, start_point, end_point):
        assert isinstance(start_point, Point), 'start point ,ust be type point '
        assert isinstance(end_point, Point), 'end point ,ust be type point '
        self.__start_point = start_point
        self.__end_point = end_point

    @property
    def start_point(self):
        return self.__start_point

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, new_end_point):
        assert isinstance(new_end_point, Point), 'must be type point '
        self.__end_point = new_end_point

    def length(self):
        d = math.sqrt((((self.start_point.x-self.end_point.x)**2)+(self.__start_point.y-self.__end_point.y)**2))
        d = round(d, 2)
        print(f'line distance is : {d}')





