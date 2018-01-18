'''
class Product:
    # Default Constructor.
    def __init__(self):
        self.productid = 10
        self.productname = "Ashok"
        
_instance = Product()
print(_instance.productid)
'''

class Product:
    # This is Constructor.
    # We can have only one constructor in Python.
    def __init__(self, ids, name):
        self.productid = ids
        self.productname = name
        
_instance = Product(10, "Ashok")
print(_instance.productid)
print(_instance.productname)

# Here SeasonProduct is extending Product
class SeasonProduct(Product):
    def __init__(self, ids, name):
        self.productid = ids
        self.productname = name
        
_instance = SeasonProduct(100, "Ram")
print(_instance.productid)
print(_instance.productname)