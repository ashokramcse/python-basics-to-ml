# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 03:17:20 2018

"""
import requests

response= requests.get("http://jsonplaceholder.typicode.com/users")
print(response)

for user in response.json():
    print(user['name'],'\t',user['email'],'\t',user['address']['city'])
    

finData=requests.get("https://www.quandl.com/api/v3/datasets/OPEC/ORB.json",verify=False)
print(finData)
print(finData.json()['dataset'])

directionsData=requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=Bangalore&destination=Pune",verify=False)
print(directionsData.json()['routes'][0]['bounds'])
