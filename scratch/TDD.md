# Test-Driven Development

## I. Introduction to Testing

A. Importance of Testing

      1. Ensuring code reliability
      2. Catching bugs early
      3. Facilitating code changes

B. Types of Testing

      1. Unit Testing
      2. Integration Testing
      3. Functional Testing
      4. System Testing

## II. Introduction to pytest

A. Installing pytest

B. Basic Concepts

      1. Test Functions
      2. Assert Statements
      3. Running Tests

C. Writing Basic Tests with pytest

      1. Test for Success
      2. Test for Failure
      3. Test for Exception

D. Advanced pytest Features

      1. Fixtures
      2. Parametrization
      3. Mocking

## III. Test-Driven Development (TDD)

A. TDD Cycle: Red-Green-Refactor

      1. Write a Failing Test (Red)
      2. Make the Test Pass (Green)
      3. Refactor Code (Refactor)

B. Importance of TDD

      1. Design before Code
      2. Regression Testing
      3. Simplifying Debugging

C. TDD Example 1. Writing the First Test 2. Implementing the Functionality 3. Refactoring

## IV. Practical Exercise

A. Implement a Small Feature Using TDD
B. Write Various Types of Tests Using pytest

### Lesson Details

#### I. Introduction to Testing

- **Importance of Testing**: Explain testing is essential for ensuring code reliability, reducing bugs in production, and making it easier to modify code in the future.
- **Types of Testing**: There are various testing levels, from unit testing to system testing, with different purposes and differences.

#### II. Introduction to pytest

- **Installing pytest**: Installing pytest using pip.
- **Basic Concepts**: basic pytest concepts like test functions, assert statements, and how to run tests.
- **Writing Basic Tests with pytest**: How to write basic tests, testing for successful outcomes, failures, and exceptions.
- **Advanced pytest Features**: Overview of advanced features like fixtures for setup code, parametrization for running a test with different inputs, and mocking to isolate unit tests.

#### III. Test-Driven Development (TDD)

- **TDD Cycle**: Red-Green-Refactor cycle and how it helps to design code and catch issues early.
- **Importance of TDD**: How TDD can help design better systems, provide regression testing, and simplify debugging.
- **TDD Example**: Simple example to demonstrate the TDD cycle.

#### IV. Practical Exercise

- Implement a feature or function using the TDD approach, Writing a test first, making it pass, and then refactoring.
- Practice writing various types of tests with pytest.

### II. Introduction to pytest

#### A. Installing pytest

Install pytest using pip. This can be done using the following command in the terminal:

```bash
pip install pytest
```

#### C. Writing Basic Tests with pytest

##### 1. Test for Success

Imagine we have a function that adds two numbers:

```python
def add(a, b):
    return a + b
```

A basic test to ensure that the `add` function works correctly might look like this:

```python
def test_add():
    assert add(2, 3) == 5
```

To run the test, save it in a file, say `test_example.py`, and run the following command in the terminal:

```bash
pytest test_example.py
```

##### 2. Test for Failure

Think about how the function might fail. For example, what if the inputs aren't numbers?

```python
def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)
```

Here, we’re expecting a `TypeError` when trying to add a string and a number.

#### III. Test-Driven Development (TDD)

##### A. TDD Cycle

###### 1. Write a Failing Test (Red)

Let’s say we want to implement a function, `multiply`, that multiplies two numbers. Start by writing a test before the function is defined:

```python
def test_multiply():
    assert multiply(2, 3) == 6
```

Running this test with pytest will fail because the `multiply` function is not defined yet.

###### 2. Make the Test Pass (Green)

Now, define the `multiply` function to make the test pass:

```python
def multiply(a, b):
    return a * b
```

Now, the test should pass when run with pytest.

###### 3. Refactor Code (Refactor)

If necessary, refactor the code. In this simple example, no refactoring is needed. But in real-world scenarios, this step might involve optimizing the code, changing variable names to be more descriptive, etc., without changing the external behavior of the code.

#### IV. Practical Exercise

##### A. Implement a Small Feature Using TDD

Implement a feature to subtract two numbers together using the TDD approach.

Start with a failing test:

```python
def test_subtract():
    assert subtract(2, 3) == -1
```

Then, implement the function:

```python
def subtract(number, other_number):
    return number - other_number
```

Implement a feature to multiply two numbers together using the TDD approach.

Start with a failing test:

```python
def test_multiply():
    assert multiply(2, 3) == 6
```

Then, implement the function:

```python
def multiply(number, other_number):
    return number * other_number
```

Implement a feature to divide two numbers together using the TDD approach.

Start with a failing test:

```python
def test_divide():
    assert divide(2, 3) == 0.6666666666666666
```

Then, implement the function:

```python
def divide(number, other_number):
    return number / other_number
```

Implement a feature to compare numbers together using the TDD approach.

Start with a failing test:

```python
def test_compare():
    assert compare(2, 2) == True
```

Then, implement the function:

```python
def compare(number, other_number):
    return number == other_number
```

##### B. Write Various Types of Tests Using pytest

Write different types of tests for the `add, subtract, multiply, divide`
function, such as:

- Test for negative numbers
- Test for non-numeric inputs
- Test for floating-point numbers
- Test for large numbers
- Test for division by zero

##### C. Discussion of where the tests should be written

- Should the tests be written in the same file as the code?
  - Answer: No, the tests should be written in a separate file.
- Should the tests be written in a separate folder?

##### D. Discussion of how to run the tests

- How to run the tests?
  - Answer: Run the tests using the `pytest` command in the terminal.
  - How to run a specific test?
    - Answer: Use the `-k` flag to run tests that match a certain keyword.

##### E. Create the calculator.py file with the previous methods a seperate test_calculator.py file with the previous tests

```python
# calculator.py
def add(number, other_number):
    return number + other_number

def subtract(number, other_number):
    return number - other_number

def multiply(number, other_number):
    return number * other_number

def divide(number, other_number):
    return number / other_number

def compare(number, other_number):
    return number == other_number
```

```python
# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, compare

def test_add():
    assert add(2, 3) == 5

def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(2, 3) == 0.6666666666666666

def test_compare():
    assert compare(2, 2) == True
```

##### F. Run the tests

```bash
pytest test_calculator.py
```

##### G. Run a specific test

```bash
pytest -k add
```

##### H. Run a specific test with verbose output

```bash
pytest -k add -v
```

##### I. What is Fixture?

A fixture is a function that is run before each test. Fixtures are used to provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results.

Example:

```python
import pytest
@pytest.fixture
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42
```

##### J. What is Parametrization?

Parametrization is a feature that allows one to run a test with multiple different inputs.

Note: We did not learn about List Comprehensions yet, so we will come back to this later.
