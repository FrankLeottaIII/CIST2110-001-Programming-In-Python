## Dealing with Python Exceptions

# Python has a built-in error handling system called exceptions. Exceptions are
# raised when something unexpected occurs during program execution. When an
# exception is raised, the program immediately stops and the interpreter prints
# the exception message. Exceptions are useful because they tell you what went
# wrong and where it went wrong. You can use this information to fix your code
# and prevent the exception from being raised again.

# The following code raises a ZeroDivisionError exception because you cannot
# divide by zero. The interpreter prints the exception message and the program
# stops.

# print(5 / 0)

# Another common exception is the FileNotFoundError exception. This exception
# is raised when a file cannot be found. The following code raises a
# FileNotFoundError exception because the file cats.txt does not exist.

# with open('cats.txt') as file_object:
#     contents = file_object.read()

# How would we handle the FileNotFoundError exception? We can use a try-except block. (This is a Try-Catch block in Java)

# Try-Except Blocks:
# The try-except block is similar to the if-else statement. The try block
# contains the code that might raise an exception. Code that depends on the
# try block executes only if the try block does not raise an exception. The
# except block tells Python what to do in case a certain exception is raised.
# The following code handles the ZeroDivisionError exception by printing a
# message instead of raising the exception.

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")


# The following code handles the FileNotFoundError exception by printing a
# message instead of raising the exception.

try:
    with open('week-9/cats.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file cats.txt does not exist.")

# You can also use try-except blocks to handle multiple exceptions. The
# following code handles both the ZeroDivisionError and FileNotFoundError
# exceptions.

try:
    print(5 / 0)
    with open('week-9/cats.txt') as file_object:
        contents = file_object.read()
except ZeroDivisionError:
    print("You cannot divide by zero!")
except FileNotFoundError:
    print("The file cats.txt does not exist.")
    
# You can also use a try-except-else block. The else block contains code that
# should run only if the try block was successful. The following code handles
# the FileNotFoundError exception by printing a message instead of raising
# the exception.

try:
    with open('week-9/cats.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file cats.txt does not exist. -HERE")
else:
    print(contents)


# you can also use a try-except-else block to handle multiple exceptions. The
# following code handles both the ZeroDivisionError and FileNotFoundError
# exceptions.

try:
    print(5 / 0)
    with open('week-9/cats.txt') as file_object:
        contents = file_object.read()
except ZeroDivisionError:
    print("You cannot divide by zero!")
except FileNotFoundError:
    print("The file cats.txt does not exist.")
else:
    print(contents)
    
    
# You can also use a try-except-else-finally block. The finally block contains
# code that should run no matter what. The following code handles the
# FileNotFoundError exception by printing a message instead of raising the
# exception.

try:
    with open('week-9/cats.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file cats.txt does not exist. -FINALLY")
else:
    print(contents)
finally:
    print("The program has finished running.")
