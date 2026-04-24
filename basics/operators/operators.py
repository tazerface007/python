# Python Program to demonstrate Operators in python.

def ArithmeticOperators():
    """Provide functionalities for Arithmentic operations"""
    print(f"{'*'*10} Arithmetic Operators {'*'*10}")
    a,b = 2,3
    print(f'a:{a}, b:{b}')
    print(f'a-b: {a-b}, type: {type(a-b)}')
    print(f'a+b: {a+b}, type: {type(a+b)}')
    print(f'a*b: {a*b}, type: {type(a*b)}')
    print(f'a/b: {a/b}, type: {type(a/b)}')
    print(f'a%b: {a%b}, type: {type(a%b)}')
    print(f'a**b: {a**b}, type: {type(a**b)}')


def AssignmentOperators():
    print(f"{'*'*10} Assignment Operators {'*'*10}")
    a = 50
    b = 20
    print(f'a: {a}, b: {b}')
    a+=2
    print(f'a+=2: {a}')

def RelationalOperators(): # Also called Comparison Operators
    print(f"{'*'*10} Relational Operators {'*'*10}")
    a = 50
    b = 20
    print(f'a: {a}, b: {b}')
    print(f'a==b: {a==b}')
    print(f'a!=b: {a!=b}')
    print(f'a>=b: {a>=b}')
    print(f'a<=b: {a<=b}')

def LogicalOperators():
    """Provide Basic logical operations on boolean numbers"""
    print(f"{'*'*10} Logical Operators {'*'*10}")
    a,b = 3,3
    print(f'a: {a}, b: {b}')
    print(f'a+3>3 and a+2>2: {(a+3 > 3 and a+2>2)}')
    print(f'a+3<3 and a+2>2: {(a+3 < 3 and a+2>2)}')
    print(f'a+3>3 or a+2<3: {(a+3 > 3 or a+2>2)}')



def BitwiseOperators():
    """Operates on Bitwise of the value"""
    print(f"{'*'*10} Bitwise Operators {'*'*10}")
    a,b = 3,2
    print(f'a: {a}, b: {b}')
    print(f'a&b: {a&b}')
    print(f'a|b: {a|b}')
    print(f'a^b: {a^b}')
    print(f'!b: {not b}')
    

if __name__ == '__main__':
    ArithmeticOperators()
    
    LogicalOperators()
    
    BitwiseOperators()

    RelationalOperators()

    AssignmentOperators()