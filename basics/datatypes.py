# Datatypes in Python

print("========= PYTHON DATA TYPES =========\n")

# 1. NoneType - Represent absence of value
none_value = None
print("1. NoneType:")
print(f"  none_value = {repr(none_value)} (type: {type(none_value)})") 
print()


# 2. Numeric Types
print("2. Numeric Types:")
int_num = 42
float_num = 3.14159
complex_num = 3+4j
print(f"\tint: {repr(int_num)} (type: {type(int_num)})")
print(f"\tfloat: {repr(float_num)} (type: {type(float_num)})")
print(f"\tcomplex: {repr(complex_num)} (type: {type(complex_num)})")

# 3. Character/String Types
print("3. String Types:")
str_value = 'Hello World'

print(f'\tstring: {repr(str_value)} (type: {type(str_value)})')


# 4. List type
print("4. List types:")
my_list = [1,2,3,4,5,6,7,8,9,10,'A','Z']
print(f'\tlist: {repr(my_list)} (type: {type(my_list)})')


# 5. Misc type (custom)
class custom_type:
    def __init__(self):
        self.name: str
        self.age: int

obj = custom_type()
print(f'\tcustom type: {repr(obj)} (type: {type(obj)}')
