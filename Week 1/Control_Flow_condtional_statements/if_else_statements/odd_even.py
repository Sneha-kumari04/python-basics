"""
Problem: Take a number from user & check the number is even or odd.
Approach: Using if-elif & if-else statements.
"""
n = int(input("Enter a number:"))

if n >0:
      if n % 2 == 0:
        print("EVEN Number!")
      elif n % 2 != 0:
         print("ODD Number!")
else:
    print("Invalid number")
