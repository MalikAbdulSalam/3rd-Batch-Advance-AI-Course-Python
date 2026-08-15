employee_ID  = input("please enter the Employ ID      ")
employee_Name = input("please enter the Employee Name       ")
employee_salary = input("please enter the Employee Salary       ")
employee_overtime = input("please enter the Employee Overtime       ")
emloyee_overtime_rate = input("please enter the Employee Overtime Rate      ")
employee_performance = input("please enter the Employee Performancec score      ")
employee_taxes = input("please enter the Employee Taxes percentage      ")



# print(employee_ID)
# print(type(employee_ID))


# Convert into integers
employee_ID = int(employee_ID)
employee_salary = int(employee_salary)
employee_overtime = int(employee_overtime)
emloyee_overtime_rate = float(emloyee_overtime_rate)
employee_performance = int(employee_performance)
employee_taxes = int(employee_taxes)



# printing all
print(employee_Name)
print(employee_salary)
print(employee_overtime)
print(emloyee_overtime_rate)
print(employee_performance)
print(employee_taxes)


Overtime_Pay = employee_overtime * emloyee_overtime_rate

print(Overtime_Pay)


employee_performance += 2

print("=" * 20)
print(employee_performance)