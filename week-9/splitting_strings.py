# In pythong you can split strings into lists using the .split() method


# Example 1
# Splitting a string into a list
# .split() will split a string into a list
# .split() takes in an argument called a delimiter

str = "Hello World! My name is Greg Hilston"

str.split() # -> ['Hello', 'World!', 'My', 'name', 'is', 'Greg', 'Hilston']

# save the list into a variable
str_list = str.split()

# print the list
print(str_list) # -> ['Hello', 'World!', 'My', 'name', 'is', 'Greg', 'Hilston']

# print for each loop with f-string
for word in str_list:
    print(f"Word: {word}")



# Example 2
print(str.split("!")) # -> ['Hello World', ' My name is Greg Hilston']


# In python we can also strip strings
# strip() will remove whitespace from the beginning and end of a string
# strip() takes in an argument called a delimiter

# Example 1
str = "    Hello World! My name is Greg Hilston     "
print(str)
print(str.strip()) # -> "Hello World! My name is Greg Hilston"