# Python Lists
# List
# Lists are used to store multiple items in a single variable.

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# List Items
# List items are ordered, changeable, and allow duplicate values.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# List Length
# to determine how many items a list has, use the len() function:
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# List Items - Data Types
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1)
# print(list2)
# print(list3)

# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# type()
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# The list() Constructor
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# Python Collections (Arrays)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Items
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# Negative Indexing
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# Range of Indexes

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# The search will start at index 2 (included) and end at index 5 (not included).

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# Range of Negative Indexes

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")