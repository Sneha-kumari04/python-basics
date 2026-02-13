"""
Problem : Take user monthly salary as input & calculate yearly salary, estimated tax(20%) and net salary'.
"""
monthly_salary = float(input("Enter your Monthly salary:"))
yearly_salary = monthly_salary * 12
tax_salary = yearly_salary * 0.20
net_salary = yearly_salary - tax_salary

print("Your Yearly Salary is  : ", yearly_salary)
print("Your Estimated tax(20%) :", tax_salary)
print("Your Net Salary is  : ", net_salary)