#%%
#Problem 1
#submit in git and canvas
y = 5.88
print(y)
print(type(y))
x = 6
print(x)
print(type(x))
z = [2,4,6,8]
print(z)
print(type(z))
a = "Great big dogs fight alligators"
print(a)
print(type(a))
# %%
#Problem 2
y = 5.88
x = 6
b = y + x
print(b)
print(type(b))
d = y - x
print(d)
print(type(d))
e = y * x
print(e)
print(type(e))
f = y/x
print (f)
print(type(f))
g = x % y
print (g)
print(type(g))
# %%
#Problem 3
s = "hi daniel"
s_upper = s.upper()
print(s_upper)
s_lower = s.lower()
print(s_lower)
s_title = s.title()
print(s_title)
s_replace = s.replace(" ","!")
print(s_replace)
# %%
#Problem 4
v = [3,6,9,12]
v.append(15)
print(v)
v.insert(0,4)
print(v)
v.insert(5,0)
print(v)
v.reverse()
print(v)
# %%
#Problem 5
d = {
    "name": "Ophelia",
    "age": 15,
    "hobbies": ["cooking", "Muay Thai", "reading", "wrestling"]
}
print(d)
d["gender"]="female"
print(d)
print(type(d))
if "hobbies" in d:
    print("Yes, 'hobbies' is in dict")
d.pop("gender")
print(d)
# %%
