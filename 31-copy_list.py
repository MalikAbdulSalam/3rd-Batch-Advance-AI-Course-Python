a ="digiboost"
b=a
print(a)
print(b)
a= "i changed"
print(a)
print(b)


# copy list by its location in memory
print("========================================")
thislist = ["apple", "banana", "cherry"]
a = thislist
print(thislist)
print(a)
thislist.append("orange")
print("after")
print(thislist)
print(a)




# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)




# Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)