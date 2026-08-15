# Create a Tuple:

thistuple = ("apple", "banana", "cherry", "alksdjflksj", "cherry")
print(thistuple)

t = type(thistuple)
print(t)
# thistuple.append("?")



list1 = [1, 2, 3]
list1.append(4)
print(list1)


# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))




print("================================")
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)



# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")


# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))



# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)