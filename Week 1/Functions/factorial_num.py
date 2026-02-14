"""
Problem: Write a program to find factorial of a number by using functions.
"""
n = int(input("Enter a number:"))

def calc_fact(n):
    fact =1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(n)