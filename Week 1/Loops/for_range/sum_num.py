"""
Problem: Sum of first n numbers 
Approach: Using for loop with range(1, n+1).
"""
n = int(input("Enter a number:"))

sum =0
for i in range(1, n+1):
    sum += i

print("sum = ", sum)