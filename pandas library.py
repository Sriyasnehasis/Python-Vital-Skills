#pandas data structure - Series , dataframe, panel
# To use pandas, make sure it is installed in your environment.
# You can install it by running: pip install pandas in your terminal.

import pandas as pd
a = pd.Series()
print(a)

x = [1, 72, 34, 4, 5]
var = pd.Series(x)
print(var)

#indexing
var =  pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(var)

#name parameter
var = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='Numbers')
print(var)

#create series using dictionary 
dict = {"Languages": ["Python", "Java" ] , "IDE": "PyCharm", "Version": 3.8}
var = pd.Series(dict)
print(var)

#single data series
s =pd.Series(12)
print(s)

#creating multi series of same data 
s = pd.Series([12, 13, 14, 15])
print(s)

#add two series
s1 = pd.Series(12 , index = [1, 2, 3])
s2 = pd.Series(13 , index = [1, 2, 3, 4])
s3 = s1 + s2
print(s3)

#DATAFRAMES
#create dataframes
#1 with the help of list 
#2 with the help of dictionary

l =[1,2,3,4,5]
var = pd.DataFrame(l)
print(var)

d = {"a": [1, 2, 3], "b": [4, 5, 6]}
var = pd.DataFrame(d)
print(var)

#show particular column
var = pd.DataFrame(d, columns = ["a"])
print(var)

#index
var = pd.DataFrame(d, columns = ["a"], index = ["a", "b", "c"])
print(var)

#get particular data
d ={"a": [1, 2, 3], "b": [24, 75, 86] , "c": [71, 8, 89]}
var2 = pd.DataFrame(d)
print(var2)
print(var2["b"][1])

#creation of DF using list 
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var3 = pd.DataFrame(lst)
print(var3)

#creation of DF using series
s1 ={"s": pd.Series([1, 2, 3]), "t": pd.Series([4, 5, 6])}
var4 = pd.DataFrame(s1)
print(var4)

#Arithmetic operations 
var = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(var)
#add another column
var["C"] = [4,7,2]
print(var)

var["D"] = var["A"] + var["B"]
print(var)

#logical operators in df 
var["Python"] = var["A"] <= 2
print(var)

#DELETE AND INSERT IN PANDAS
#INSERT
import pandas as pd
var = pd.DataFrame({"A":[1,2,3,4], "B" : [5,6,7,8]})
print(var)
# total 3 parameteers to insert - index , coloumn , data
var.insert(2 , "C", [9, 10, 11, 12])
print(var)
#DELETE
var = pd.DataFrame({"A":[1,2,3,4], "B" : [5,6,7,8]})
var.pop("C")
print(var)

# we can also use del instead of pop 
del var["B"]
print(var)


