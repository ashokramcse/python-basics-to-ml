# -*- coding: utf-8 -*-
'''
Spyder Editor

This is a temporary script file.
'''

print("Hello World!")

firstName = "Ashok" #input("Enter Name: ")
print("Customer Name is: %s"%(firstName))
print(type(firstName))

#Type conversion
# Number, String, List, Tuple and Dictonary
# Numbers - int, long(1065L), float and complex(3.14j)

age = int("15") #int(input ("Enter Age: "))
print("Age = %d"%(age))
print(type(age))

#Decimal to Binary
print(bin(10))

#Binary to Decimal
print(int("1010", 2))

# Center Justification
orgName="CITI"
print(orgName.center(len(orgName)+20, "*"))

# Left and Right Justification
print(orgName.ljust(len(orgName)+20, "*"))
print(orgName.rjust(len(orgName)+20, "*"))
amount = "1234"
print(amount.rjust(len(amount)+20, " "))

"""
Sequence Number generator
"""
import base64
seqNo = 456

data = base64.b64encode(str(seqNo).encode(encoding = 'utf-8', errors='strict'))
print("Converted Data is : %s \n" %(data))

for _d in data[0:]:
    print(chr(int(_d)), end="")
print("\n")

'''
List in python is heterogeneous.
'''
data = [45,"Ashok", 46.5, "C", True]
print(data)

for _ in data:
    if(type(_) is str):
        print(_)

'''
Generate Random Number
'''
import random
idList = []

for _ in range(10):
    idList.append(random.randint(1, 1000))

print(idList)
idList.sort()
idList.reverse()
print(idList)

empList = [[1, "Ashok", "Chennai"], [2, "Ram", "Bangalore"]]

for row in empList:
    for _ in row:
        if (_ is "Chennai"):
            print(row[1])

list1 = ["Chennai", "Bangalore"]
list2 = ["TN", "KA"]

for (x,y) in zip(list1, list2):
    print(x, ","+y)

#Join & Split Operation
print((",").join(list1))
print(((",").join(list1)).split(","))

# Tuples are immutable
# Tuple which hold only one data can treat as const

data = (56, "Ashok", "Chennai")
data1 = (57, "Ashok", "Chennai")

print(data.__add__(data1))
print(data)

#Dictonary
customers = {"Key1":"Value1","Key2":"Value2","Key3":"Value3"}
print(customers)
print(customers.keys()) # List of Keys
print(customers.values())

for(key, value) in customers.items():
    print(key, value)
    
cust = {"Key1":{"Key1":"Value1","Key2":"Value2","Key3":"Value3"},
        "Key2":{"Key1":"Value1","Key2":"Value2","Key3":"Value3"},
        "Key3":{"Key1":"Value1","Key2":"Value2","Key3":"Value3"}}
print(cust)
print(cust.keys()) # List of Keys
print(cust.values())

for(key, value) in cust.items():
    print(key, value)