# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Unchangeable

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Tuple Length

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# Create Tuple With One Item

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# Tuple Items - Data Types

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# print(tuple1)
# print(tuple2)
# print(tuple3)

# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Tuple Items

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# Negative Indexing

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# Range of Indexes

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# Range of Negative Indexes

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# Check if Item Exists

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# Add Items

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# Remove Items

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a Tuple

# fruits = ("apple", "banana", "cherry")
# print(fruits)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# Using Asterisk*

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# Loop Through a Tuple

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# Loop Through the Index Numbers

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# Using a While Loop

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# Join Two Tuples

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# Multiply Tuples

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# Tuple Methods

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found