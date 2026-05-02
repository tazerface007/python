"""Multi level Inheritance"""

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat():
        pass

    def poop():
        pass

    def fart():
        pass

class Person(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def walk():
        pass

class Man(Person):
    def __init__(self, name, age, height, weight):
        super().__init__( name, age, height)
        self.weight = weight


if __name__ == '__main__':
    obj = Man("Deepak", 26, 182, 85)
    print(f'Hello, {obj.name}')
    print(f'age, {obj.age}')
    print(f'Height, {obj.height}')
    print(f'Weight, {obj.weight}')
