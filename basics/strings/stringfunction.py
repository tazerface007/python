a = 'Hello, World'

print(a.upper())

print(a.lower())

print(a.capitalize())

print(a.strip())


# String Concatenation

a1 = 'Hello'

b1 = 'World'

c = a1 + ' ' + b1

print(c)


# Python String format

price = 59.9

txt = f'The price is {price} dollars'

print(txt)

# A placeholder can include a modifier to format the value.

"""
A modifier is included by a colon ':' followed by a legal formatting type, like .2f which means fixed point number with 2 decimals.
"""

txt2 = f'The price is {price:.2f} dollars'
print(txt2)


# Escape Character

print("We are the so-called \"Vikings\" from the north.")