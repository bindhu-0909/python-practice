# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# Dictionary Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# Changeable

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# Dictionary Length

# print(len(thisdict))

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(len(thisdict))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Accessing Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

# Get Keys

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# Update Dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# Adding Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)

# Removing Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)