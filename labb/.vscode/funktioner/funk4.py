# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def showEmployee(name, salary=9000):
    print("Name:", name, "salary:", salary)

showEmployee("Ben", 12000)
showEmployee("Jessa")

# Name: Ben salary: 12000
# Name: Jessa salary: 9000

# Default arguments take the default value during the function call if we do not pass them. We can assign a default value to an argument in function definition using the = assignment operator.

# # function with default argument
# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)