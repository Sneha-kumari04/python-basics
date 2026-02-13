"""
Problem: The sum of first n numbers 
Approach: using while loop.
"""
n = int(input("Enter the number:"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of n numbers is = ", sum)