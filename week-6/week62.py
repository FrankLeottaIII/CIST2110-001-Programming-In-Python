# Python Debugging

# Examples using the debugger

COUNTER = 0


def print_numbers():
    for i in range(10):
        print("Index: " + str(i))
        global COUNTER
        COUNTER += 1
        print("COUNTER: " + str(COUNTER))



def main():
    print_numbers()

if __name__ == "__main__":
    main()
