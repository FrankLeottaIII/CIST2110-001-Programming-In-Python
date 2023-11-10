# In python there are multiple ways to print variables

# 1. Using the print() function
# 2. Using the format() function
# 3. Using f-strings

name = "Greg"
last_name = "Hilston"

# 1. Using the print() function
print("Hello World!")
print(name + " " + last_name) # -> with string concatenation

# 2. Using the format() function
# Denoted by the {} curly braces
# You can use variables inside the curly braces
# .format() is a method that can be called on a string
print("Hello World! My name is {} {}".format(name, last_name)) # -> with format()

# 3. Using f-strings
# Denoted by the f before the string
# You can use variables inside the curly braces
print(f"Hello World! My name is {name} {last_name}") # -> with f-strings


# f-strings with loops and conditionals
# f-strings can be used inside loops and conditionals

# for loop
for i in range(1, 11):
    print(f"Hello World! My name is {name} {last_name} and I am {i} years old")
