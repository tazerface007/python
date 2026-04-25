# Strings in python

Strings in python are surrounded by either single quotation mark or double quotation marks.

In Python 'hello' is same as 'Hello'


## Multi-line Strings

```python
a = """Hello World,
    How are you? Hope you are good.
```


## ***Python - Slicing Strings***

***Slicing***

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, seperated by a colon, to return a part of the string.

```python
b = 'Hello, World!'
print(b[2:5])
```

## Escape Character

To insert characters that are illegal in a string, use an escape character.

A escape character is a backslash '\' followed by the character you want to insert.

An example of an illegel character is a double inside a string that is surrounded by double quotes:

```python
txt = "We are the so-called \"Vikings\" from the north."
```