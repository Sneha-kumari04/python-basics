"""
Problem: Simple calculator using if-elif-else statements.
Approach: Take two numbers and user choice and perform selected operations.
"""

num1 = float(input("Enter first number = "))
num2 = float(input("Enter second number = "))

print(" \nChoose operations:")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")

choice = input("Enter your choice = ")

if choice == "1":
    print("Result = ", num1 + num2)
elif choice == "2":
    print("Result =", num1 - num2)
elif choice == "3":
    print("Result = ", num1*num2)
elif choice == "4":
    print("Result = ", num1/num2)
else:
    print("Invalid choice")

