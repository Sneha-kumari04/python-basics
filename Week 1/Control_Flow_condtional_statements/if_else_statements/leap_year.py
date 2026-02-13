"""
Problem: Check whether a year is leap year or not.
Approach: Applying leap year conditions and using if-elif-else statements.
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")