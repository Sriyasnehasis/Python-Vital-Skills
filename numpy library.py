#creating rrays in numpy 
import numpy as np 
a  = np.array([1, 2, 3, 4, 5])
print("Array:", a)

import numpy as np
x = [1, 2, 3, 4, 5]
b = np.array(x)
print("Array:", b)

#create array by user input 
l=[]
for i in range(1,5):
    inp = int(input("Enter numbers: "))
    l.append(inp)

print("Array:", np.array(l))

#dimensions in array - 1D, 2D, 3D , higher dimensions
y = np.array([1, 2, 3])
print("1D Array:", y)
y.ndim  # prints 1

z = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:", z)
print("Dimensions of 2D Array:", z.ndim)  # prints 2

w = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:", w)
print("Dimensions of 3D Array:", w.ndim)  # prints 3

#higher dimensions
arr = np.array([1,2,3,4]) , ndmin = 10
print("Higher Dimensional Array:", arr)

#create numpy arrays with random numbers
# 1.rand() - generates random numbers between 0 and 1
# 2.randn() - generates random numbers from standard normal distribution , close to 0 , may be +ve / -ve
# 3.randf() - generates random numbers between 0 and 1 - > [0.0 , 1.0]
# 4. randint() -> generates random integers within a specified range

#rand()
import numpy as np
var = np.array.rand(4)
print("Random Array (rand):", var)

var1 = np.array.rand(2,3)
print("Random 2D Array (rand):", var1)

#randn()
var2 = np.random.randn(4)
print("Random Array (randn):", var2)

#randf()
var3 = np.random.randf(4)
print("Random Array (randf):", var3)

#randint()
# var4 = np.random.randint(min , max . total_values)
var4 = np.random.randints(1, 10, 5)
print("Random Integers (randint):", var4)

var5= np.random.randint(1, 10, (2, 3))
print("Random 2D Integers (randint):", var5)

#datatypes in numpy arrays 
#Difference between paython arrays and numpy arrays 
# 1. Python arrays can hold any data type, while NumPy arrays are homogeneous (all elements must be of the same type).
# 2. NumPy arrays are more efficient for numerical operations due to their fixed data types and contiguous memory layout.
# 3. NumPy provides a wide range of mathematical functions that can be applied to arrays, while Python arrays do not have this capability.
# 4. NumPy arrays support multi-dimensional arrays, while Python arrays are typically one-dimensional.
# 5. NumPy arrays are implemented in C, making them faster for numerical computations compared to Python arrays.
# 6. NumPy arrays have a fixed size, while Python arrays can grow dynamically.
# 7. NumPy arrays support broadcasting, allowing operations on arrays of different shapes, while Python arrays do not.
# 8. NumPy arrays can be sliced and indexed in more complex ways than Python arrays.
# 9. NumPy arrays can be reshaped, while Python arrays cannot.
# 10. NumPy arrays can be saved to and loaded from files in binary format, while Python arrays do not have this feature.
# 11. NumPy arrays can be used with various mathematical libraries, while Python arrays are not as widely supported.

#bool_
#int_
#Intc
#Intp
#Int8 and more

import numpy as np
var = np.array([1,2,3,4])
print("Data Type: " , var.dtype)  # prints int64 or int32 depending on the system

#datatype can be changed
x =np.array([1, 2, 3, 4], dtype=np.float64)
print("Data Type after conversion:", x.dtype)  # prints float64

#arithmetic operations
a+b = np.add(a,b)
a-b = np.subtract(a,b)
a*b = np.multiply(a,b)
a/b = np.divide(a,b)
a%b = np.mod(a,b)
a**b = np.power(a,b)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", np.add(a, b))  # prints [5 7 9]
var1= a/3
print("Division:", np.divide(a, 3))  # prints [0.33333333 0.66666667 1.        ]

#reciprocal 
print("Reciprocal:", np.reciprocal(a))  # prints [1.         0.5        0.33333333]




             


