"""
Problem: To determine the  grade of a student based on their marks. 
Approach: Using if-elif & if-else statements.
"""
marks = int(input("Enter your marks:"))

if marks > 0:
    if marks >= 80 and  marks <= 100:
        print("Bravo!! , your grade is A")
    elif marks >=65 and marks < 80:
        print(" Well tried!!, your grade is B")
    elif marks >= 50 and marks < 65:
        print(" Your grade is C")
    elif marks >=33 and marks < 50:
        print("Your grade is D")
    elif  marks < 33:
        print("Fail!!!!")
else:
    print("Please enter your right marks:")