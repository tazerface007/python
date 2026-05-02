# Object Oriented Programming in Python

OOP stands for Object-Oriendted programming.

- Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

## Advantages of OOPS

- Provides a clear structure to program.
- Makes code easier to maintain, reuse and debug.
- Helps keep your code DRY(Don't Repeat Yourself).
- Allows you to build reusable application with less code.

## What are Classes and Objects?

Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class.

- Almost everything in python is an object, with its properties and methods.
- A class is like an object constructor, or a 'blueprint' for creating objects.

**Create a class**:

```python
class Myclass:
    x = 5
```
**Create Object**:

```python
p1 = Myclass()
print(p1.x)
```

**Delete Objects**:

```python
del p1
```

**Multiple Objects**:

## Pass Statement in Python

- Class definition cannot be empty; but if for some reason have a clas definition with no content, put in the pass statement to avoid getting error

```python 
class Test:
    pass
```

## Python __init__() Method

- All classes in python inherit or contains the __init__() method.
- This method helps python classes to initialize its variable values.
- Without the __init__() method, you would need to manually set properties for each object.

**Default values in __init__()**:

- You can also set default values for parameters in the __init__() method.

*example*:

```python
class Person:
    def __init__(self, name, age=18):
        self.name = name;
        self.age = age

    p1 = Person("Rajiv")
    p2 = Person("Sameer", 18)

    print(p1.name, p1.age)
    print(p2.name, p2.age)
```


## Python Self Parameter

- The *self* parameter is the reference variable to the current instance of the class.
- It is used to access properties and methods that belong to the class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Tazerface", 25)
p1.greet()
```
***Note: The self parameter must be the first parameter of any method in the class.***

### Why use self?

Without self, Python would not know which object's properties you want to access.

### ***Self Does not have to be named "self"***

- It does not have to be named self, you can call it whatever you liek, but it has to be the first parameter of any object in the class.

***Example***:

```python
class Person:
    def __init__(this, name, age):
        this.name = name
        this.age = age
    def greet(this):
        print("Hello, my name is " + this.name)
p1 = Person("Rohit", 36)
p1.greet()
```

***Note: While you can use different name instead of "self", it is strongly recommended to use "self" as it is the convention in python and makes your code more readable.***

### Accessing properties with "self"

- you can access any property of the class using "self"

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'{self.year} {self.brand} {self.model}')
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()
```
