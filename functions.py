#syntax of functions in python 
def function_name(parameters):
    pass
    #code and statements 
#calling a function EXAMPLES
def name(fname , lname):
    print("My name is " + fname + " " + lname) 
    name("John", "Doe")  # calling the function with arguments "John" and "Doe"   
def cars():
    print("audi" , "bmw")
cars()  # calling the function to print car names

#function arguments and return statement
#1.deafault arguments
def names(fname, mname="k" , lname="Doe"):
    print("My name is " , fname , mname , lname)
names("John")  # calling the function with default middle and last names
# diff between parameters and arguments
# Parameters are the variables defined in the function signature, while arguments are the values passed to those parameters when calling the function.
def add(a,b):
    a+b
add(2,3)  # calling the function with arguments 2 and 3
print(add(2,3))  # prints the result of the addition
#2.keyword arguments
def name(fname, lname):
    print("My name is " + fname + " " + lname)
name(lname="Doe", fname="John")  # calling the function with keyword arguments
#3.required arguments
def name(fname, mname , lname):
    print("My name is " , fname , mname , lname)
name("John",  "Doe")  # calling the function with required arguments
#variable-length arguments
#there are two types of variable-length arguments in Python: *args and **kwargs.
#1.arbitrary arguments
def name(*name):
    print("Hello",name[0],name[1],name[0])
name("John", "Doe")  # calling the function with variable-length arguments
#2.keyword arbitrary arguments
def name(**name):
    print("Hello", name["fname"], name["lname"])
name(fname="John", lname="Doe")  # calling the function with keyword arbitrary arguments

#return statement
def name(fname, lname):
    return "My name is " + fname + " " + lname
print(name("John", "Doe"))  # prints the return value of the functio

#EXERCISE
#calculator using functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y
print("Select operation:")
print("1. Add") 
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
    choice = input("Enter choice (1/2/3/4): ")
   
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        
        break
    else:
        print("Invalid input. Please enter a valid choice.")

#local and global variables
x = 10
def my_function():
    y = 5 
    print(y)
#call the function 
my_function()  # prints 5
print(x) # prints 10
print(y) # raises an error because y is a local variable and not accessible outside the function

#global keyword use
x = 10  # global variable
def my_function():
    global x  # declare x as a global variable
    x = 20  # modify the global variable
my_function()  # call the function
print(x)  # prints 20, as the global variable x has been modified
print(y)  # raises an error because y is not defined outside the function

#python program using a function if a yaer is leap year or not 
def leap_year(year):
    return(year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0)

#user input for the yaer 
year = int(input("Enter a year: "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    



        

   


