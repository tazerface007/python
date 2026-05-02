# File Handling In Python 

Python has sevaral functions for creating, reading, updating and deleting files.

- The key function for working with files in python is the **open()** function.
- The **open()** function takes two parameters; filename; and mode.
- There are four different methods(modes) for opening a file:
    - ***"r"*** - Read - Default value, Opens a file for reading, error if the file does not exists.
    - ***"a"*** - Append - Open a file for appending(modifying), creates a file if not exists.
    - ***"w"*** - Write - Open a file for writing, creates the file if the file not exists.
    - ***"x"*** - Create - Creates the specified file, returns an error if the file exists.

- In addition you can specify if the file should be handled as a binary or text mode
    - ***"t"*** - Text - Default value, Text mode.
    - ***"b"*** - Binary - Binary mode (e.g. images)

### Syntax

```python
f = open("demofile.txt")
```
or 
```python
f = open("demofile.txt", "rt")
```
Both the format is same, because "r" for read and "t" for the text are the default values.
