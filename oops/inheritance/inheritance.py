# A basic inheritance demonstration in python

class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'



class Derived(Base):
    def __init__(self, name, age, salary):
        super().__init__( name, age)
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'



if __name__ == '__main__':
    obj = Derived('Deepak', 25, 500000)
    print(obj)
