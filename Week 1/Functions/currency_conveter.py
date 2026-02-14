"""
Problem: Write a program to convert USD to INR.
"""
usd_value = float(input("Enter your USD value: "))

def clac_converter(usd_value):
    inr_value = usd_value * 90.57
    print(usd_value,  "USD = ", inr_value, "INR")

clac_converter(usd_value)
