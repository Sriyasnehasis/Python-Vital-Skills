#example
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
finally:
    print("Execution completed.")

#question- create a function when the function devides 10 by a user
def divide_number():
    try:
        x = int(input("Enter a num: "))
        result = 10/x
        print("Result: ", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    else:
        print("No exception occured.")
    finally:
        print("Execution completed.")
divide_number()

#raise & assert 
#make a  program to take input from user 
quit_word = "quit"
input_str = input("Enter value:")
if quit_word == input_str:
    print(input_str)
else:
    raise ValueError("You entered an invalid value. Please enter 'quit' to exit.")

#question
num = int(input("Enter ur age:"))
if num > 18:
    print("You are eligible to vote.")
else:
    raise AssertionError("You are not eligible to vote. You must be at least 18 years old.")

def greet(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    print(f"Hello, {name}!")

try:
    greet("")
except ValueError as e:
    print("Error occured:",e)

#ques1
a = int(input("Enter a number which is greater than 5 : "))
if a<5:
    raise ValueError("The number must be greater than 5.")
