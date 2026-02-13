"""
Problem: Find the largest numbers among the numbers entered by user.
Approach: Compare the numbers by using if-elif-else conditions.
"""
a = int(input("Enter the number 1 = "))
b = int(input("Enter the number 2 = "))
c = int(input("Enter the number 3 = "))

if a > b and a > c:
    print("Number 1 is largest number")
elif b > c and b > a:
    print("Number 2 is largest number")
elif c > a and c > b:
    print("Number 3 is largest number")
else:
    print("Invalid numbers")
