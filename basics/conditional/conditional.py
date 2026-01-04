# Conditional statements in python

if False:
    print('fuck you')
elif (a:=23): # walrus operator
    print('ok')
else:
    print('nice to meet you')

# testing if 0 is false

if 0:
    print('Hello')

# testing if class is positive
class test:
    def __init__(self):
        pass

if test:
    print('eww')

if 0j or 0.0 or 0:
    print('awk')
