'''
Examine the code below and troubleshoot it.

Objective: This function should take two numbers and return their division, but handle it properly if there is a problem.

Your tasks:

-This code will throw a ZeroDivisionError if num2 = 0. Handle this error.
-If the user enters a non-numeric value (e.g. hello), a ValueError will be thrown. Handle this error.
-After the function is executed, display a message saying "The program ran successfully!", even if an error occurs.
-The program should not crash! Instead, it should prompt the user for valid input.
'''

def divide(a, b):
    return a / b


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:",divide(num1, num2))

except ValueError:
    print("Error: please enter valid integers.")

except ZeroDivisionError:
    print("Error: cannot divide by zero.")

else:
    print("Result:", divide(num1, num2))

finally:
    print("The program run successfully.")



