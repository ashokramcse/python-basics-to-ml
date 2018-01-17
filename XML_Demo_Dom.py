# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 03:30:07 2018

"""

from xml.dom import minidom
#create DOM object
doc=minidom.Document()

rootElement=doc.createElement("Customers")
doc.appendChild(rootElement)
node=doc.createElement("Customer")
node.setAttribute('CustomerId','12345')
rootElement.appendChild(node)

accountNode=doc.createElement("Account")
node.appendChild(accountNode)

accountNo=doc.createElement("AccountNo")
text = doc.createTextNode('4334645')
accountNo.appendChild(text)
accountNode.appendChild(accountNo)

xml_str = doc.toprettyxml(indent="  ")
with open("citrixcustomerdata.xml", "w") as f:
    f.write(xml_str)

doc = minidom.parse("citrixcustomerdata.xml")

routers=doc.getElementsByTagName("Customers")

for router in routers:
    print(router.getElementsByTagName("Customers")[0].firstChild.data)
    interfaceData=router.getElementsByTagName("AccountNo")
    for interface in interfaceData:
        print(interface.getElementsByTagName("AccountNo")[0].firstChild.data)