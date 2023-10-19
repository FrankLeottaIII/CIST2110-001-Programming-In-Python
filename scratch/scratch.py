# 6. Write some code that asks the user for a number, then prints out all the numbers from 1 to that number. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

input_number = int(input("Enter a number: "))
for i in range(1, input_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
# LAB


# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.

input_number = int(input("Enter a number: "))
if input_number > 0:
    print("The number is positive.")
elif input_number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
input_number = int(input("Enter a number: "))
if input_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
    
# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
input_number = int(input("Enter a number: "))
counter = 1
while counter <= input_number:
    print(counter)
    counter += 1
    
    
# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.

total = 0
for i in range(5):
    number = int(input("Enter a number: "))
    total += number
average = total / 5
print("The average of the numbers is", average)


# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        print(i)


# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
input_number = int(input("Enter a number: "))
while input_number >= 1:
    print(input_number)
    input_number -= 1
print("Blast off!")


# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.

# Ask the user for a number
num = int(input("Please enter a number: "))

# Use a for loop to iterate from 1 to that number
for i in range(1, num + 1):
    # If the current number is divisible by 7, print "Lucky" and continue to the next iteration
    if i % 7 == 0:
        print("Lucky")
        continue
    # If the current number is greater than 100, break the loop
    if i > 100:
        break
    # Print the current number
    print(i)