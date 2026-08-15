# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "name": "hafiz saab"
}

inputt = input("Enter any key to continue...")


if inputt in thisdict:
  print("Yes, inputt"" is one of the keys in the thisdict dictionary")
else:
  print("No, inputt is one of the keys in the thisdict dictionary")