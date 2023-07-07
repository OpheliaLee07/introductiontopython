#%%
#Problem 1
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    print(item)
# %%
hello = ["joe","bob","jeremy","patricia","violet","john"]
for name in hello:
    z = "hello " + name 
   # print(z)
    z_title = z.title()
    print(z_title)
# %%
lst = [1,2,3,4,5,6,7,8,9,10]
total = sum(lst)
print(total)
# %%
string = "cheese" [::-1]
print(string)
# %%
string = "alachua"
string_dict = {}
for i in string:
    if i in string_dict.keys():
        string_dict[i]+= 1
    else:
        string_dict[i] = 1

for i in string_dict.keys():
    print(f"{i}: {string_dict[i]}")

    
   # %%
scores = {
    "Jeremy": 50,
    "Trevor": 77,
    "Klaus":49,
    "Francheska": 96,
    "Lila":89,
    "Yolanda":67,
    "John": 60,
    "Lia": 61,
    "Reina": 84
}
for x,y in scores.items():
    if y >= 60:
        print("pass",x, y)
#%%
num = 7
count = 1
while count <= 10:
    print(f"{num}x {count}= {num*count}")
    count += 1

# %%
#Problem 2
i=1
while i < 11:
    print(i)
    i+=1
# %%
print("Please enter your name:")
string = " " 
x = True
while x == True:
    string = input("Please enter your name:")
    if string == "quit":
        x= False
    else:
        print("Hello "+ string)
# %%
print("Please enter a number: ")
x = input(" ")
if  int(x) % 2 == 0:
    print("even")
elif int(x) % 2 != 0:
    print("odd")
else:
    print("n/a")

# %%
import random
print(lst)
rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(0,100))
print("list: ", rand_list)
rand_list.sort()
print("smallest number: ", rand_list[0])
print("biggest number: ", rand_list[9])
# %%
fruits = {
    "apple": 0.75,
    "pear": 1.25,
    "peach": 1.00,
    "watermelon":4.75,
    "dragonfruit": 3.25,
    "banana" : 1.60,
    "orange" :0.70
    }
print("Enter a fruit")
z = input(" ")
if z in fruits:
     print(z,fruits[z])
else:
    print("Sorry, we don't have that fruit")
# %%
    