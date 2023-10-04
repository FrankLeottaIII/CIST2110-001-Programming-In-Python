## Python main function

# Import the module week52.py
import week52

name = "Greg"
height = 6.0

def main():
    # week52.test_me("Greg")
    week52.print_person_attributes(name,26,height)
    account_balance = week52.print_account_balance(1000.00)
    print(account_balance)

    account_balance2 = week52.return_account_balance(5000.00)
    account_balance2 += 1000.00

    new_account_balance = week52.print_account_balance(account_balance2)

    print(new_account_balance)

    account_balance3 = week52.return_account_balance()

    print(week52.print_account_balance(account_balance3))
    week52.print_person_attributes(name="Greg",age=26,height=6.0)

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()
