


thislist = ["apple", "banana", "cherry"]
print(thislist[2])


# Print the last item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



# Return the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# This example returns the items from "cherry" to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Check if "apple" is present in the list
thislist = ["apple", "banana", "cherry"]

flag = "apple" in thislist

print("Value of Flag is                        " + str(flag))


if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  print("Yes, 'apple' is in the fruits list")
  print("Yes, 'apple' is in the fruits list")
  print("Yes, 'apple' is in the fruits list")
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")