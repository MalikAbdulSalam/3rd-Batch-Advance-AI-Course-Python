# Convert the tuple into a list to be able to change it:

a = 56
a =str(a)
b = "568"
int(b)
b = float(b)




x = ("apple", "banana", "cherry")
y = list(x)     #convert tupple to list

print(x)
print(y)

print(type(x))
print(type(y))


y[1] = "kiwi"
x = tuple(y)  #convert backin to tupple
print(x)



# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("new value of tupls is  ",thistuple)


# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y  # thistuple = thistuple + y

print(thistuple)


# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists