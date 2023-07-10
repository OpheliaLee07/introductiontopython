#%%
def custom_print(my_string):
     # This function prints my_string

    print(my_string)
custom_print("hello world")
custom_print(my_string="hello world")
# %%
custom_print("world hello")
# %%
def add_three_variables(x, y, z):
    # mathematical function
    return x + y + z
add_three_variables(1,2,3)
g = add_three_variables(5,6,7)
print(g)
# %%
def list_maker(my_string, n=5):
    #function that returns a list of the string repeated a certain amount of times
    lst = [my_string] * n
    return lst
lst = list_maker("daniel", 2)

# %%
def dict_changer(data, operation="capitalize"):
    # Iterate through the values of a dictionary and perform a string operation on it.
    #if type(data) != dict:
    if not isinstance(data, dict):
        print("ERROR: Please input a dictionary for data")

    if operation == "capitalize":
        for key in data.keys():
            data[key] = data[key].capitalize()
    elif operation == "lower":
        for key in data.keys():
            data[key] = data[key].lower()
    elif operation == "title":
        for key in data.keys():
            data[key] = data[key].title()
    elif operation == "remove.2":
        for key in data.keys():
            data[key] = data[key][:-2]
    else:
        print("ERROR. I don't support any other operation")
    return data
data = {
    "name": "daniel",
    "location": "New York City",
    "drinking":"coffee",
    "using":"Python"
}
ndata = dict_changer(data, operation="remove 3")
print(ndata)
# %%
string_multiplier = lambda string: string*5 + " " + string
string_multiplier("daniel")
# %%
def list_splitter(my_string, n=2):
    if type(my_string) != str:
        return("Error: Please enter a string.")
    lst = my_string.split()

    if len(lst) > n:
        for i in range(n-1, len(lst), n):
            print(i)
            lst[i] = lst[i].capitalize()
    return lst

list_splitter("this is an example problem")
list_splitter(3)
# %%
import numpy 

value = numpy.random.randint(0,100)

# %%
import numpy as np
value = np.random.randint(0,100)

# %%
from numpy import arange, sin
a = arange(0,10)
b = sin(a)
# %%
import numpy as np
def add_sin_cos(min=0, max=10, step=10):
    np.linspace()
# %%
