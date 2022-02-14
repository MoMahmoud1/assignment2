class Student:
    def __init__(self, id: int, name: str, address: str, program: str, current_courses: [], completed_courses: {}):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__program = program
        self.__current_courses = current_courses
        self.__completed_courses = completed_courses

    # @property
    def name(self):
        return self.__name

    # @property
    def id(self):
        return self.__id

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def average_score(self):
        total = 0
        for i in self.__completed_courses.value():
            total += i
        if total > 1:
            return total/len(self.__completed_courses.value)

        else:
            return -1

    def add_course(self, new_course):
        self.__current_courses.append(new_course)

    def drop_course(self, course_id):
        for course in self.__current_courses:
            if course == course_id:
                self.__current_courses.remove(course)
            else:
                raise ValueError

    def course_completed(self, course_id, marks_obtain):
        if course_id in self.__current_courses:
            self.__completed_courses[course_id] = marks_obtain
        else:
            print('course not found')
