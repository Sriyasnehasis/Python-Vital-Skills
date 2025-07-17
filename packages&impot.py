#import 
import math
result = math.sqrt(16)
print("The square root of 16 is:", result)

#from keyword
from math import sqrt
result = sqrt(25)
print("The square root of 25 is:", result)

from math import pi
print("The value of pi is:", pi)

#as keyword
import math as m
result = m.pow(2, 3)
print("2 raised to the power of 3 is:", result)

#import everything
from math import *
result = sin(pi / 2)
print("The sine of pi/2 is:", result)

#dir function 
import math
print("Available functions and constants in the math module:")
print(dir(math))

