#%%
#Problem 1 
print("Please enter a word: ") 
x = input(" ")
is_palindrome = x [::-1]
for y in x:
    if x == is_palindrome:
        print("True")
        break
    else:
     print("False")
     break

#%%
#Problem 2
import numpy as np

class Rectangle(object):
   def __init__(r,length,width):
      r.length = length
      r.width = width
   def calculate_area(r,length,width):
      return length * width
   def calculate_perimeter(r,length,width):
      return length+length+width+width
   
NewRectangle = Rectangle (length=5, width = 4)
print(Rectangle.calculate_area(r= 0, length=5, width = 4))
print(Rectangle.calculate_perimeter(r=0, length= 5, width = 4))
# %%
#Problem 3 
def count_words(lst):
    diction = {}
    for x in lst:
        if x in diction:
            diction[x] += 1
        else:
            diction[x] = 1
    for key,value in diction.items():
       print(key,value)

lst = ["baguette", "chicken", "baguette", "chicken", "chicken", "croissant"]
count_words(lst)
#%%

#%%
# %%
