# Simple script to greet the user
# Get the user's name as input
# Write a program that receives an option from an user
# If opt1, ask for 2 numbers, and add them up.
# If opt2, ask for 2 numbers, and substract them.
# If opt3, ask for 2 numbers, and multiply them.
# If opt4, ask for 2 numbers, and divide them.
# If opt5, exit.
# If it gives any other option other than 1, 2, 3, 4, 5, print "Invalid Option"

# Ask for a user name, why not?

import math
from decimal import Decimal, getcontext

# Set the precision to 10 decimal places (adjust as needed)
getcontext().prec = 10

user = input("What's your name? ")
print(" ")
# Print a greeting message

print("Hello, " + user + "! Welcome to Basic Calculator.")

    # Ask the user the type of operator needed
print("What type of operation do you want to do today?")
print(" ")
while True:
    print("Please choose from the following:")
    print("Addition press '1'.")
    print("Substraction press '2'.")
    print("Multiplication press '3'.")
    print("Division press '4'.")
    print("To exit press '5'.")

    # Get user's choice as input
    user_choice = input("Enter the number of your choice: ")
    print(" ")

    # Check the user's choice and ask for numbers needed for the operation
    # Addition #1
    if user_choice == '1':
        print("Great so let's start: ")
        str_num1 = Decimal(input("Please type first number: "))
        str_num2 = Decimal(input("Now, type second number: "))
        num1 = (str_num1)
        num2 = (str_num2)
        result = num1+num2
        value = (result)
        print("Great! So this is the result hun: ")
        print(value)
    # Substraction #2
    elif user_choice == '2':
        print("Great so let's start: ")
        str_num1 = Decimal(input("Please type first number: "))
        str_num2 = Decimal(input("Now, type second number: "))
        num1 = (str_num1)
        num2 = (str_num2)
        result = num1-num2
        value = (result)
        print("Great! So this is the result hun: ")
        print(value)
    # Multiplication #3
    elif user_choice == '3':
        print("Great so let's start: ")
        str_num1 = Decimal(input("Please type first number: "))
        str_num2 = Decimal(input("Now, type second number: "))
        num1 = (str_num1)
        num2 = (str_num2)
        result = num1*num2
        value = (result)
        print("Great! So this is the result hun: ")
        print(value)
    # Division #4
    elif user_choice == '4':
        print("Great so let's start: ")
        str_num1 = Decimal(input("Please type first number: "))
        str_num2 = Decimal(input("Now, type second number: "))
        num1 = (str_num1)
        num2 = (str_num2)
        result = num1/num2
        value = (result)
        print("Great! So this is the result hun: ")
        print(value)
    # To exit #5
    elif user_choice == '5':
        continue_choice = input("Are you sure you want to close me? (y/n): ")
        if continue_choice.lower() != 'no' and continue_choice.lower() != 'n':
            print(" ")
            print("Thank you " + user + " if you need something else,")
            print("Just run the program again!")
            break
        print(" ")
    else:
        print("Invalid input. Please choose 1, 2, 3, 4 or 5.")
        print(" ")
    # First project
