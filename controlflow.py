
#star pattern 
i=1
while i <= 5:
 print(i * '*')
 i = i+1

#hello pattern
i=1
while i <= 7:
 print(i * 'Hello ')
 i += 1

#inverted triangle star pattern
 rows = 5
 for i in range(rows , 0 , -1):
  print('*' * i )

# a right angle triangle of stars
 rows = 5
 for i in range (i , rows+1):
  print('' * (rows - i) + '*' * i) 

#break 
names= ["a","b","c","d","e"]
for name in names:
  if (name == "c"):
   break
  print(name)

#continue
  names= ["a","b","c","d","e"]
  for name in names:
    if (name == "c"):
     continue
    print(name)
   
search_list = [1,2,3,4,5]
target = int(input("Enter the no to search: "))

for num in search_list:
  if num == target:
   print("NO found!")
   break

else:
  print("no not found!")
  
   
 
  
  


 
