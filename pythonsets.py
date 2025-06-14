# Set
# Sets are used to store multiple items in a single variable

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates Not Allowed

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)

# thisset = {"apple", "banana", "cherry", False, True, 0}

# print(thisset)

# Get the Length of a Set

# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))

# Set Items - Data Types

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# print(set1)
# print(set2)
# print(set3)

# set1 = {"abc", 34, True, 40, "male"}
# print(set1)

# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# Access Items

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}

# print("banana" not in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# Add Items

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# Add Any Iterable

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# Remove Item

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)

# Loop Items

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3)

# Join Multiple Sets

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)

# Update

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)

# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
