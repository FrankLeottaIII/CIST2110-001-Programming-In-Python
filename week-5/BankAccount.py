# Simple Bank Account Management System

# Create a bank account program that will authenticate a user and allow them to deposit, check balance, and withdraw money from their account.
# Also create a Main Menu that will look like the following:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# Functions:
# User Authentication() -> Boolean (True or False) - Return True if username and pin are correct, otherwise return False
# Main Menu - Return the user's choice (int)
# Menu Logic - attempt to call the appropriate function based on the user's choice
# Check Balance(balance) -> Float - Return the user's balance
# print Balance(balance) -> None - Print the user's balance
# Deposit(amount) -> Float - Return the user's balance after depositing the amount
# Withdraw(amount) -> Float - Return the user's balance after withdrawing the amount

# Some things to consider:
# Error Handling
# Proper Comments and Documentation
# Include main statement


# Global Variables
# Global Variables - Variables that are accessible to all functions
# In this program we will have 3 global variables
# 1. username
# 2. pin
# 3. balance

USERNAME = "JDoe52" # random username
PIN = "1234" # random pin
BALANCE = 10000.00 # random balance


# Functions
# authenticate_user() -> Boolean

def authenticate_user() -> bool:
    """_summary_
    This function authenticates the user by asking for their username and pin
    The funtion will only prompt 3 times for the username and pin

    Args:
        None

    Returns:
        bool: True if username and pin are correct, otherwise return False
    """

    # create a for loop that counts from 0 to 2 (3 times total)
        # Ask user for username
        # Ask user for pin
        # Check if username and pin are correct
    # Return True if username and pin are correct, otherwise return False

    for i in range(3): # 0 1 2
        input_user = input("Enter username(Case Sensitive): ")
        # Error Handling:
        # remove any spaces from the input
        input_user = input_user.strip()
        # If the user enters nothing, ask them to enter a username using a while loop
        while input_user == "":
            print("You did not enter a username. Please try again.")
            input_user = input("Enter username(Case Sensitive): ")
            input_user = input_user.strip()

        input_pin = input("Enter pin: ")
        # Error Handling:
        # remove any spaces from the input
        input_pin = input_pin.strip()
        # If the user enters nothing, ask them to enter a pin using a while loop
        while input_pin == "":
            print("You did not enter a pin. Please try again.")
            input_pin = input("Enter pin: ")
            input_pin = input_pin.strip()

        if input_user == USERNAME and input_pin == PIN:
            return True
        else:
            print("Invalid username or pin. Please try again. You have " + str(2-i) + " attempts left.") # 2-i = 2-0 = 2, 2-1 = 1, 2-2 = 0
            #TODO - Possibly fix the Please try again with 0 attempts left
        if i == 2:
            print("You have exceeded the maximum number of attempts. Goodbye.")
            return False
    return False # by default return False

def check_balance() -> str:
    """_summary_
    This function checks the user's balance

    Args:
        None

    Returns:
        str: "Your account balance is: $" + str(balance)
    """
    return "Your account balance is: $" + str(BALANCE)

def print_balance() -> None:
    """_summary_
    This function prints the user's balance

    Args:
        None

    Returns:
        None
    """
    print(check_balance())

def deposit(amount=None) -> float:
    """_summary_
    This function deposits money into the user's account

    Args:
        amount (float): The amount to deposit

    Returns:
        float: The user's balance after depositing the amount
    """
    global BALANCE # global keyword allows us to access the global variable BALANCE
    if amount is None:
        amount = float(input("Please Enter Amount to deposit: $"))
    BALANCE += amount
    print("You have deposited $" + str(amount))
    return BALANCE

def withdraw(amount=None) -> float:
    """_summary_
    This function withdraws money from the user's account

    Args:
        amount (float): The amount to withdraw

    Returns:
        float: The user's balance after withdrawing the amount
    """
    global BALANCE # global keyword allows us to access the global variable BALANCE
    # Error Handling:
    # What if the user enters a negative number or a 0?
    # Use a while loop to ask the user to enter a positive number
    if amount is None:
        print("Your current balance is: $" + str(BALANCE))
        amount = float(input("Please Enter Amount to withdraw: $"))

    while amount <= 0:
        print("You cannot withdraw a negative number or $0. Please try again.")
        amount = float(input("Please Enter Amount to withdraw: $"))

    # What if the user enters a number greater than their balance?
    while amount > BALANCE:
        print("You cannot withdraw more than your balance. Please try again.")
        amount = float(input("Please Enter Amount to withdraw: $"))

    BALANCE -= amount
    print("You have withdrawn $" + str(amount))
    return BALANCE

def main_menu() -> int:
    """_summary_
    This function prints the main menu and returns the user's choice

    Args:
        None

    Returns:
        int: The user's choice
    """
    print("Main Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))
    # Error Handling:
    # What if the user enters a number less than 1 or greater than 4?
    # Use a while loop to ask the user to enter a number between 1 and 4
    while choice < 1 or choice > 4:
        print("Invalid choice. Please try again.")
        choice = int(input("Please enter your choice: "))
    return choice


def menu_logic(choice: int) -> None:
    """_summary_
    This function calls the appropriate function based on the user's choice
    Should only be called in conjunction with the main_menu() function

    Args:
        choice (int): The user's choice from the main menu (1, 2, 3, or 4) - this is checked in the main_menu() function

    Returns:
        None
    """
    if choice == 1:
        print_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Goodbye")
        exit()
    else:
        print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Bank of Python Please authenticate yourself.")
    if authenticate_user() is True: # alternatively if authenticate_user(): can be used
        print("Authentication successful.")


    # Error Handling:
    # Keep Prompting the user to enter a choice until they enter 4
    while True:
        choice = main_menu()
        menu_logic(choice)
        if choice == 4:
            print("Goodbye")
            exit()
        else:
            choice = main_menu()
            menu_logic(choice)

    # Testing Functions
    #authenticate_user()
    # print(check_balance())
    # print_balance()
    #deposit(7000.00)
    #deposit()
    # withdraw()
    # print_balance()
    # choice = main_menu()
    # menu_logic(choice)
    # could also do this:
    # menu_logic(main_menu())

if __name__ == "__main__":
    main()
