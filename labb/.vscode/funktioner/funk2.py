# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

# Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

def func1(*argument):
    for a in argument:
        print(a)

func1("Hej")
func1(1, 2, 30)
func1("Julia")

# To accept a variable length of positional arguments, i.e., To create functions that take n number of positional arguments we use *args as a parameter. (prefix a parameter name with an asterisk * ).

# Using this, we can pass any number of arguments to this function. Internally all these values are represented in the form of a tuple.

# Read: variable length of arguments in functions
# Function call:
# # call function with 3 arguments
# func1(20, 40, 60)

# # call function with 2 arguments
# func1(80, 100)
    
# Expected Output:
# Printing values
# 20
# 40
# 60
    
# Printing values
# 80
# 100