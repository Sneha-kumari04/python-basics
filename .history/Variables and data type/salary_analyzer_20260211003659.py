"""
This program :
- Takes user monthly salary as input
- Calculate Yearly salary and tax  salary
- Prints yaerly and tax salary

"""
monthly_salary = float(input("Enter your Monthly salary:"))
yearly_salary = monthly_salary * 12
tax_salary = yearly_salary * 0.20

print("Your Yearly Salary is  : ", yearly_salary)
print("Your Estimated tax(20)")