#bar plot 
import matplotlib.pyplot as plt
x =["Python", "Java", "C++", "JavaScript"]
y = [10, 20, 15, 25]
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.bar(x, y , width = 0.4, color = ["black", "red", "green", "blue"] , edgecolor = "black" , linestyle = "dashed")
plt.show()

#scatter plot 
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
c = ['red', 'blue', 'green', 'orange', 'purple']  # colors for each point
plt.xlabel("Day" , fontsize=14 , color='blue')
plt.ylabel("Number of Visitors" , fontsize=14 , color='blue')
plt.title("Scatter Plot Example")
plt.scatter(x, y, color='blue', marker='*', s=100)  # s is the size of points
plt.show()

#writec a program to draw a scatter plot comparing two subject marks of students
import matplotlib.pyplot as plt
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
math_marks = [85, 90, 78, 92, 88]
science_marks = [80, 85, 82, 88, 90]
plt.xlabel("Math Marks", fontsize=14, color='blue')
plt.ylabel("Science Marks", fontsize=14, color='blue')
plt.title("Scatter Plot Comparing Subject Marks")
plt.scatter(math_marks, science_marks, color='blue', marker='o', s=100)
plt.show()

#Line plot 
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.xlabel("X-axis", fontsize=14, color='blue')
plt.ylabel("Y-axis", fontsize=14, color='blue')
plt.title("Line Plot Example")
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.show()

#draw a line plot to draw a V shape and an inverted V shape
import matplotlib.pyplot as plt
x_v = [1, 2, 3, 2, 1]
y_v = [1, 2, 1, 0, 1]
x_inv_v = [1, 2, 3, 2, 1]
y_inv_v = [1, 0, 1, 2, 1]
plt.xlabel("X-axis", fontsize=14, color='blue')
plt.ylabel("Y-axis", fontsize=14, color='blue')
plt.title("V Shape and Inverted V Shape")
plt.plot(x_v, y_v, color='blue', marker='o', linestyle='-',
            linewidth=2, markersize=8, label='V Shape')
plt.plot(x_inv_v, y_inv_v, color='red', marker='x', linestyle='--',
            linewidth=2, markersize=8, label='Inverted V Shape')
plt.legend()
plt.show()

#pie chart 
import matplotlib.pyplot as plt
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [30, 25, 20, 25]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
explode = (0.1, 0, 0, 0)  # explode the first slice (Python)
plt.xlabel("Programming Languages", fontsize=14, color='blue')
plt.ylabel("Popularity", fontsize=14, color='blue')
plt.title("Popularity of Programming Languages")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()

#donut chart
import matplotlib.pyplot as plt
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [30, 25, 20, 25]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=140, pctdistance=0
        , wedgeprops=dict(width=0.3))  # width for donut effect
plt.title("Popularity of Programming Languages (Donut Chart)")
plt.show()

#3D plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.sin(np.sqrt(x**2 + y**2))
ax.plot3D(x, y, z, 'blue')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Line Plot Example')
plt.show()

#count plot
import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('titanic')
sns.countplot(x='class', data=data, palette='Set2')
plt.xlabel("Passenger Class", fontsize=14, color='blue')
plt.ylabel("Count", fontsize=14, color='blue')
plt.title("Count of Passengers by Class")
plt.show()





