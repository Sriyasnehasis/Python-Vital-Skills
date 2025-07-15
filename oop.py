#how to create a class using CLASS keyword
class Details:
    name = "Sriya"
    age = 20
#create a object 
obj1 = Details()
# to print value 
class Details:
    name = "Sriya"
    age = 20
obj1 = Details()
print("Name:", obj1.name)
print("Age:", obj1.age)
#self parameter
class Details:
    name = "Sriya"
    age = 20
#creating self parameter
    def desc(self):
        print("Name:", self.name)
        print("Age:", self.age)
obj1 = Details()
obj1.desc()  # prints Name: Sriya Age: 20

#parameterized constructor
class Details:
    def __init__(self, name, age):
      self.name = name
      self.age = age
obj1= Details("Sriya", 20)
print("Name:", obj1.name)
print("Age:", obj1.age)

#deafault constructor 
class Details:
    def __init__(self):
        print("This is a default constructor")
obj1 = Details()  # prints This is a default constructor

#inhertiance in python 
#single inheritance
class Parent:
    def func1(self):
        print("This is parent class function")
class Child(Parent):
    def func2(self):
        print("This is child class function")
object=Child()
object.func1()  # prints This is parent class function
object.func2()  # prints This is child class function

#2.multiple inheritance
class Mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    
    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father:", self.fathername)
        print("Mother:", self.mothername)

s1 = Son()
s1.fathername = "John"
s1.mothername = "Jane"
s1.parents()  # prints Father: John Mother: Jane

#polymorphism
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

def aninmal_says(Animal):
    return Animal.speak()
dog = Dog()
cat = Cat()
print(aninmal_says(dog))  # prints Woof!
print(aninmal_says(cat))  # prints Meow!

#practice questions of OOPS
#create a calcuator using python 
class calculator:
    def add(self , x , y):
        return x+y
    
    def sub(self, x, y):
        return x-y
    
    def mul(self, x, y):
        return x*y
    
    def div(self, x, y):
        return x / y
calc = calculator()

result_add = calc.add(5,3)
print("Addition result:", result_add)
result_sub = calc.sub(5,3)
print("Subtraction result:", result_sub)
result_mul = calc.mul(5,3)
print("Multiplication result:", result_mul)
result_div = calc.div(5,3)
print("Division result:", result_div)

#inheritance question 
def __init__(self, name):
    self.name = name
def speak(self):
    return "Unknown sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says", dog.speak())
print(cat.name, "says", cat.speak())

#design a class called rectangle it should have attributes length and width and calculate area and perimeter
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return self.length * 2 + self.width * 2
    def is_square(self):
        return self.length == self.width
    
rectanagle = Rectangle(5, 10)
print("Area:", rectanagle.area())
print("Perimeter:", rectanagle.perimeter())
print("Is square:", rectanagle.is_square())

rectangle2 = Rectangle(5, 5)
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())
print("Is square:", rectangle2.is_square())

    





        
    



    
        


