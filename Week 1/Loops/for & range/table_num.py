"""
Problem: Print the multiplication table of a number n
Approach: Using for loop with range(1, 11).
"""
n = int(input("Enter the number:"))
for i in range(1,11):
    print(n * i)