import pytest

# imagine we have a function that adds 2 numbers and returns the result

# 1. Write a basic test that ensures the function returns the correct result

# first example of pytest (notice the assert statement)

def test_add():
    assert add(2, 3) == 5

# run this code in your terminal with the following command:
# pytest week6_test_example.py



# 2. Write the function to make the test pass

def add(a, b):
    return a + b


# 3. Write a test that ensures the function raises a TypeError if the arguments are not numbers

def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)


# Implement a function that multiplies 2 numbers and returns the result. Start by writing a test before the function.

def test_multiply():
    assert multiply(2, 3) == 6 

def multiply(a, b):
    return a * b

def test_subtract():
    assert subtract(5, 3) == 2

def subtract(a, b):
    return a - b

def test_divide():
    assert divide(6, 3) == 2

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)
        
        
        
def test_compare():
    assert compare(2,2) == True
    assert compare(2,3) == False

def compare(a, b):
    return a == b

def main():
    print(divide(3, 0))
    # test_add()
    
if __name__ == "__main__":
    main()