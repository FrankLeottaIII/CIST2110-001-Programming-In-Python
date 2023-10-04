def test_me(name):
    print("Hello " + name + "!")
    return "I returned"

# functions can have multiple parameters
# Last class we saw examples of functions with no 
# parameters, functions with 1 parameter. This is an 
# exampl of a function with 3 parameters.
def print_person_attributes(name: str, age: int, height:float) -> str:
    """_summary_
    This function prints the name, age, and height of a person

    Args:
        name (str): Users name
        age (int): Users age
        height (float): Users height

    Returns:
        str: "I returned"
        also returns the name, age, and height
    """
    print("Name: " + name)
    print("Age: " + str(age))
    print("Height: " + str(height))
    return "I returned"

def print_account_balance(balance: float) -> str:
    return "Your account balance is: $" + str(balance)
def return_account_balance(balance=10000.00) -> float:
    return balance


def a(name: str, age: int, height:float) -> str:
    print("Dont ever do this")

def main():
    test_me("John")
    test_me("Mary")
    test_me("Bob")

if __name__ == "__main__":
    main()
