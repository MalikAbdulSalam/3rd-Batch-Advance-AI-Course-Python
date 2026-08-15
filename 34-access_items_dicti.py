# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]



# Get the value of the "model" key:
x = thisdict.get("model")

# Get a list of the keys:
x = thisdict.keys()
print(x)



# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,

}

x = car.keys()  # get key and assign to x

print(x) #before the change

car["color"] = "white"
car["condition"] = "genuine";

print(x) #after the change
print(car)




# Get a list of the values:
y= car.keys()
x = car.values()
print(x)
print(y)