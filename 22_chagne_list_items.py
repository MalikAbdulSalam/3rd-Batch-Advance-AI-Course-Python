thislist = ["apple", "banana", "cherry"]

thislist[1] = "blackcurrant"
print(thislist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon" ,"ezan"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# Change the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)




# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)



# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]


thislist.extend(tropical)
print(thislist)
print(tropical)


# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)