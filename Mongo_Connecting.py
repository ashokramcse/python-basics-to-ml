# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:35:03 2018

Files used in Mongo DB folder
mongod = Server file
mongo = Client file

To start Mongo DB server use
mongod --port 27017 --dbpath=C:\Users\RPS\Desktop\Ashok\Mongo

To start Mongo DB client use
mongo --port 27017

Comments
--------
# Show all db's
show dbs;

# To create DB, Untill we add collections to the db's it will not create a db.
use employeedb;

# To show all the collections
show collections;

# Employees is the collection
db.employees.insert({empId:123,name:"Ashok",dob:new Date(1991,10,4)});

# Search documents from the collections.
db.employees.find();

#To create a document
var employee={empId:456,name:"Ram",dob:new Date(1991,8,6)};

#Add the created document
db.employees.insert(employee);

"""

from pymongo import MongoClient
 
#connect to the MongoDB.
conn = MongoClient('localhost',27017)
 
#Access the testdb database and the customer collection.
db = conn.empdb.customers
 
#create a dictionary to hold customer details.
 
#create dictionary.
cust_rec = {}
 
#set flag variable.
flag = True
 
#loop for data input.
while (flag):
   #ask for input.
   cust_name,cust_addr,cust_id = input("Enter customer name, address and id: ").split(',')
   #place values in dictionary.
   cust_rec = {'name':cust_name,'address':cust_addr,'id':cust_id}
   #insert the record.
   db.insert(cust_rec)
   #Ask from user if he wants to continue to insert more documents?
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False
 
#find all documents.
ret = db.find()
 
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
 
#display documents from collection.
for record in ret:
	#print out the document.
	print(record['name'] + ',',record['address'] + ',',record['id'])
 
print()
 
#close the conn to MongoDB
conn.close()
