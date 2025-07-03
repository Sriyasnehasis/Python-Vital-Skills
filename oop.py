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



