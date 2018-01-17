# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("Hello World!")

firstName = "Ashok" #input("Enter Name: ")
print ("Customer Name is: %s"%(firstName))
print (type(firstName))

#Type conversion
# Number, String, List, Tuple and Dictonary
# Numbers - int, long(1065L), float and complex(3.14j)

age = int("15") #int(input ("Enter Age: "))
print ("Age = %d" %(age))
print (type (age))

#Decimal to Binary
print (bin(10))

#Binary to Decimal
print (int("1010", 2))

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