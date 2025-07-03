#read
f = open("random.txt", "r")
content = f.read()
print(content)
f.close()
#write
f = open("random.txt", "w")
f.write("This is a new line added to the file.\n")
f.close()
#append
f = open("random.txt", "a")
f.write("This line is appended to the file.\n")
f.close()
#question
f = open("random.txt", "w")
lines = {"line 1" , "line 2", "line 3"}
for line in lines:
    f.write(line + "\n")
f.close()
#with statement 
with open("random.txt", "r") as f:
    content = f.read()
    print(content)

#readlines method 
f =open("random.txt", "w")
f.write("This is a new line added to the file.\n")
f.close()

f=open("random.txt", "r")
f.read()

f= open("random.txt", "r")
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line , type(line))
        break
#writelines method
f = open("random.txt", "w")
lines = ["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"]
f.writelines(lines)
f.close()

f = open("random.txt", "r")
f.read()

#seek() and tell () methods
f =open("random.txt", "w")
write = f.write("This is a new line added to the file.\n")
print(write)
f.close()

with open("random.txt", "r") as f:
    print(type(f))
    f.seek(10)
    data = f.read(5)
    print(data) 

with open("random.txt", "r") as f:
    print(type(f))
    f.seek(10)
    print(f.tell())  # Prints the current position in the file
    data = f.read(5)
    print(data)  # Prints the data read from the file

with open("random.txt", "w") as f:
    f.write("Hello world")
    f.truncate(5)  # Truncates the file to 5 bytes
with open("random.txt", "r") as f:
    print(f.read())  # Prints the content of the file after truncation



