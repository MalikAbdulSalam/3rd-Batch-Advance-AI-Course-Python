# Copy by reference

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}



mydict = thisdict


print(mydict)

thisdict["color"] = "Black"
thisdict["Conditio"] = "Class 1"

print(mydict)


print("=========================")




# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


mydict = thisdict.copy()
print(mydict)






#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


mydict = dict(thisdict)
print(mydict)



