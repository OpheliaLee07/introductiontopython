#%%
# First expressions

x = 7
y = 5

# %%
z = x + y
# %%
INT = 5
FLOAT = 5.5
#%%
question = INT + FLOAT
# %%
x % y
# %%
10 % 5
# %%
x == y
# %%
x != y
# %%
lst = [1,2,3,4,5]
# %%
lst.append(6)
# %%
lst.insert(0,0)
# %%
lst.insert(3,10)
# %%
lst.remove(3)
# %%
new_lst =  lst[1:5]
new_lst = lst[4:]
# %%
person = {
    "name":"daniel",
    "age": 30,
    "height":6,
    "zoom":True
}
# %%
my_string="The fox jumped over the lazy dog"
# %%
string_list=my_string.split("over")
# %%
hobbies="wrestling, Muay Thai, writing"
hobbies.strip()
hobbies=hobbies.replace(" ","")
hobbies.split(",")
# %%
hobbies="and".join(hobbies)
# %%
