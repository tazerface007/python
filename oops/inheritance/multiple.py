# Python Multiple Inheritance

class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class Man:
    def __init__(self, height):
        self.height = height


    def __str__(self):
        return f' Height: {self.height}'



class Employee:
    def __init__(self, salary):
        self.salary = salary


    def __str__(self):
        return f'Salary: {self.salary}'



class Father(Base, Man, Employee):
    def __init__(self, name, age, height, salary, son):
        super().__init__(name, age)
        Man.__init__(self, height)
        Employee.__init__(self, salary)
        self.son = son

    def __str__(self):
        return f' {Base.__str__(self)}; {Man.__str__(self)}; {Employee.__str__(self)}'


if __name__ == '__main__':
    obj = Father('Deepak', 25, '6 Feet', 500000, 'Sam')
    print(obj)
