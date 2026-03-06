# Datatypes in python

"""
Python Datatypes:
1. Basic Built-in Datatypes

- Numbers:
    - int -> whole numbers (e.g. 42)
    - float -> decimal numbers (e.g. 3.14)
    - complex -> numbers with real + imaginary parts (e.g. 2+3j)

- Strings:
    - Text data, written in quotes: 'Hello', "Python"
    - Supports slicing, concatenation, formatting.

- Booleans:
    - Logical values: True or False
    - Often used in conditions.

2. Collections

- List
    - Orderd, mutable: [1, 2, 3]
    - Can hold mixed datatypes: [1, 'apple', 3.14]

- Tuple
    - Ordered, immutable: (1, 2, 3)
    - Useful for fixed data.

- Set
    - Unordered, unique elements: {1, 2, 3}
    - Great for removing duplicates.

- Dictionary
    - Key-value pairs: {"name": "Alice", "age": 25}
    - Keys must be unique and immutable

3. Advanced

- Bytes & Bytearray
    - bytes -> immutable sequence of bytes
    - bytearray -> mutable version
    - used for binary data, networking, cryptography

- Frozen Set
    - Immutable version of a set: frozenset([1, 2, 3])
    - Useful when you need hashable sets.

- Memoryview
    - Provides a view of memory for binar data without copying.
    - Efficient for large datasets.

4. Custom & Abstract Datatypes

- Classes & Objects
    - You can define your own datatypes using class.
    - Example:
        class Car:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model
        my_car = Car("Tesla", "Model S")

- Collections Module
    - Specialized datatypes:
        - namedtuple -> tuple with named fields
        - deque -> fast append/pop from both ends
        - Counter -> counts occurrences
        - defaultdict -> dictionary with default values
        - OrderedDict -> dictionary that remembers order (Python 3.7+ dicts already do)
"""

print("=========================== DATATYPES IN PYTHON ===========================")    

print("=========================== 1. Built in datatypes ===========================")

vint = 23

print(f'Integer: {repr(vint)}\t{type(vint)}')

vfloat = 2.3

print(f'Float: {repr(vfloat)}\t{type(vfloat)}')

vcomplex = 3.2 +4.3j

print(f'Complex: {repr(vcomplex)}\t{type(vcomplex)}')


vstring = 'Hello'

print(f'String: {repr(vstring)}\t{type(vstring)}')


vbool = True

print(f'Boolean: {repr(vbool)}\t{type(vbool)}')


#--------------------------------------------------------------------
print("=========================== 2. Collection types ===========================")

# Collection type

vlist = [1, 2, 3, 3, 4, 5]

print(f'List: {repr(vlist)}\t{type(vlist)}')


vtuple = (1, 2, 3, 3, 4, 5)

print(f'Tuple: {repr(vtuple)}\t{type(vtuple)}')


vset = {1, 2, 3, 3, 4, 5}

print(f'Set: {repr(vset)}\t{type(vset)}')

vdict = {
    "name": "Kishan",
    "age": 25,
    "gpa": 8.8 
}

print(f'Dictionary: {repr(vdict)}\t{type(vdict)}')


#-------------------------------------------------------------------------------
print("=========================== 3. Advanced types ===========================")

vbyte = bytes(b"Hello World")

print(f'Byte: {repr(vbyte)}\t{type(vbyte)}')


vbytearray = bytearray(b'hello World')  
vbytearray[0] = 72

print(f'Bytearray: {repr(vbytearray)}\t{type(vbytearray)}')

vfs = frozenset([1, 2, 3])
d = {vfs: "immutable set"}

print(d[vfs])


vmemview = memoryview(vbytearray)
print(vmemview)


#-------------------------------------------------------------------------------
print("=========================== 4. Collection Module ===========================")
from collections import namedtuple

print("Named Tuple")
Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)

print(p.x, p.y)

print("Deque")
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)

from collections import Counter

c = Counter("bananna")
print(c)


from collections import defaultdict

dd =  defaultdict(int)
dd["apple"] = 1
print(dd)


from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2

print(od)

#-------------------------------------------------------------------------------
print("=========================== 4. Custom Classes ===========================")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    
s = Stack()

s.push(1)
s.push(2)
print(s.pop())
