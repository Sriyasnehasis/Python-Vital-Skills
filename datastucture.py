#lists and range
lst1 = [1, 2, 3, 4, 5]
print(lst1)
print(type(lst1))

# list with mixed data types
lst2 = [1, "two", 3.0, [4], (5,)]
print(lst2)
print(type(lst2))

#list index
colors =["red", "green", "blue"]
print(colors[0])
print(colors[1])
print(colors[2])

#positive indexing
print(colors[0])  # first element
print(colors[1])  # second element
print(colors[2])  # third element

#negative indexing
print(colors[-1])  # last element
print(colors[-2])  # second to last element
print(colors[-3])  # third to last element

#check whether an item is in a list
if "red" in colors:
    print("Red is in the list")
else:
    print("Red is not in the list")

#list slicing
print(colors[0:2])  # first two elements
print(colors[-1:-2])


print(colors[0:])  # all elements

#prining alternate elements
animals = ["cat", "dog", "fish", "bird", "hamster"]
print(animals[::2])  # prints every second element 
print(animals[1:4:3])  # prints every third element starting from index 1

#list conmprehension 

#accepts items with the small letter "a"
names = ["Alice", "Bob", "Charlie", "David"]
filtered_names = [item for item in names if "a" in item]
print(filtered_names)  # prints names containing the letter "a"
#accept items which have more than 4 letter
filtered_names1 = [item for item in names if len(item) > 4]
print(filtered_names1)  # prints names with more than 4 letters
#accept items which have more than 4 letter and small letter "a"

#input from user in list
items = input("Enter items separated by commas: ").split(",")
print("Elements in the list:", items)

#list mthods 
#sorting a list
colors = ["red", "green", "blue"]
colors.sort()  # sorts the list in ascending order by default
print(colors)

colors.sort(reverse=True)  # sorts the list in descending order
print(colors)
#reversing a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # reverses the order of the list
print(numbers)
#indexing a list
colors = ["red", "green", "blue"]
index_of_green = colors.index("green")  # finds the index of "green"
print(index_of_green)
#counting occurrences of an item in a list
colors = ["red", "green", "blue", "red"]
count_of_red = colors.count("red")  # counts how many times "red" appears
print(count_of_red)
#copying a list
colors_copy = colors.copy()
print(colors_copy)
#appending an item to a list
colors.append("yellow")  # adds "yellow" to the end of the list
print(colors)
#inserting an item at a specific index
colors.insert(1, "orange")  # inserts "orange" at index 1
print(colors)   
#extending a list with another list
rainbow  = ["violet", "indigo"]
colors.extend(rainbow)  # adds all elements of rainbow to colors
print(colors)
#concatenating two lists
colors = ["red", "green", "blue"]
rainbow = ["violet", "indigo"]
combined_colors = colors + rainbow  # concatenates two lists
print(combined_colors)

#python tuples
# Tuples are immutable sequences
tup1 = (1, 2, 3, 4, 5)
print(tup1)
print(type(tup1))
#tuple indexes
tup2 = ("apple", "banana", "cherry")
print(tup2[0])  # first element
print(tup2[-1])  # last element
#checking if an item is in a tuple
if "banana" in tup2:
    print("Banana is in the tuple")
else:
    print("Banana is not in the tuple")
#range of index
#example printing elements with a particular range:
animals = ("cat", "dog", "fish", "bird", "hamster")
print(animals[1:4])  # prints elements from index 1 to 3 (4 is excluded)
print(animals[4:]) # prints elements from index 4 to the end

#python dictionaries
# Dictionaries are mutable mappings of key-value pairs
name = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}
print(name)
print(type(name))
# Accessing values in a dictionary
print(name["first_name"])  # prints "John"
print(name.values())  # prints all values in the dictionary
print(name.keys())  # prints all keys in the dictionary
print(name.items())  # prints all key-value pairs in the dictionary

#dict methods
#update() method
name.update({"age": 31})  # updates the value of "age" to 31
print(name)
#clear() method
name.clear()  # removes all items from the dictionary
print(name)  # prints an empty dictionary
#pop() method
name.pop("first_name")  # removes the key "first_name" and its value
print(name)  # prints the dictionary after removing the key
#popitem() method
name.popitem()  # removes the last inserted key-value pair
print(name)  # prints the dictionary after removing the last item
#de() method
del name["last_name"]  # deletes the key "last_name" and its value
print(name)  # prints the dictionary after deleting the key

