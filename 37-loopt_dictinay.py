# loop in dictionay


a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "name": "hafiz saab"
}


for i in a:
    print(i)
    # print(a[i])





for key,value in a.items():
    print(key, value)
    # print(a[i])

    

print("===============================")

# You can also use the values() method to return values of a dictionary:
for x in a.values():
  print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "name": "hafiz saab"
}

print("===============================")

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)













