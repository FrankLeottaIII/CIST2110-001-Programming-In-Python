# Lists and Tuples

# Lists and tuples are both types of sequences in Python. They are similar in many ways, but have some important differences.

# Lists

# A list is a collection of items that can be of any type. Lists are mutable, which means that you can change their contents.

# Creating a list
my_list = [1, 2, 3, "four", 5.0]

# Accessing elements of a list
print(my_list[0])  # 1
print(my_list[3])  # "four"

# Changing elements of a list
my_list[1] = "two"
print(my_list)  # [1, "two", 3, "four", 5.0]

# Adding elements to a list
my_list.append(6)
print(my_list)  # [1, "two", 3, "four", 5.0, 6]

# Removing elements from a list
my_list.remove("four")
print(my_list)  # [1, "two", 3, 5.0, 6]

# Slicing a list
print(my_list[1:3])  # ["two", 3]

# Tuples

# A tuple is similar to a list, but is immutable, which means that you cannot change its contents.

# Creating a tuple
my_tuple = (1, 2, 3, "four", 5.0)

# Accessing elements of a tuple
print(my_tuple[0])  # 1
print(my_tuple[3])  # "four"

# Trying to change elements of a tuple will result in an error
# my_tuple[1] = "two"  # TypeError: 'tuple' object does not support item assignment

# Tuples are often used to return multiple values from a function
def get_name_and_age():
    return "Alice", 30

name, age = get_name_and_age()
print(name)  # "Alice"
print(age)  # 30

# Conclusion

# Lists and tuples are both useful types of sequences in Python. Lists are mutable and can be changed, while tuples are immutable and cannot be changed. Choose the appropriate type based on your needs.
