#%%
class Person(object):
    def __init__(self, username, password):
        self.username = None
        self.password = None
        self.photo = None
        self.email = None
        self.phone = None

    def parse_email(self, string):
        #checks email is an email
        if "@" in string:
            return True
        else:
            return False
        
    def capitalize_name(self):
        return self.username.capitalize()

    
person = Person(username="daniel", password = "password")

# %%

class Animal(object):
    def __init_(self, name):
        self.name = None
        self.fur = None
        self.legs = None
        self.type = None
        self.sleep = False
    
    def sleeping(self):
        if self.sleep = True

def hungry(self):
    self.food_amount = 0 

def eaten(self):
    self.food_amount = 100

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        self.legs = 4

a = Animal
d = Dog (name = "Karl Marx")
#%%
import numpy as np
class Circle(object):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self, radius):
        return np.pi * radius ** 2
    
    def calculate_circumference(self, radius):
        return 2*np.pi * radius
    
Newcircle = Circle(2)
print(Newcircle.calculate_area(2))
# %%
string = "test"

string.capitalize()

# %%
