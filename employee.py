
class Employee:
    def __init__(self, first_name: str, last_name: str, employee_id: str, salary: float):
        self.__first_name = first_name
        self.__last_name = last_name
        if employee_id[0] == "E" and len(employee_id) == 5 and employee_id[1:5].isnumeric():
            self.__employee_id = employee_id
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def annual_salary(self):
        return 12 * self.__salary

    @property
    def name(self):
        return f'{self.__first_name}" "{self.__last_name}'

    def raise_salary(self, rais_percent):
        raise_amount = self.__salary * rais_percent / 100
        self.__salary += raise_amount

