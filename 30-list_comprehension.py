fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)




# sort_list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)



# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)



# sort in decending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


print("=" * 50)


# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)



# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)



# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)



# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)