"""
Problem: Print factorial of  n number 
Approach: Iterative multiplication using for loop.
"""
n = int(input("Enter the number:"))

fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial =", fact)
