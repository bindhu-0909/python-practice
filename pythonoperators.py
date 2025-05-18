# Python Operators
# print(10 + 5)

# Python Arithmetic Operators

# +	Addition	x + y	
# x = 5
# y = 3
# print(x + y)

# -	Subtraction	x - y	
# x = 5
# y = 3
# print(x - y)

# *	Multiplication	x * y	
# x = 5
# y = 3
# print(x * y)

# /	Division	x / y	
# x = 12
# y = 3
# print(x / y)

# %	Modulus	x % y	
# x = 5
# y = 2
# print(x % y)

# **	Exponentiation	x ** y	
# x = 2
# y = 5
# print(x ** y) #same as 2*2*2*2*2

# //	Floor division	x // y	
# x = 15
# y = 2
# print(x // y)
#the floor division // rounds the result down to the nearest whole numbe

# Python Assignment Operators

# =   x = 5   x = 5
# x = 5
# print(x)

# # +=	x += 3	x = x + 3
# x = 5
# x += 3
# print(x)	

# # -=	x -= 3	x = x - 3
# x = 5
# x -= 3
# print(x)

# # *=	x *= 3	x = x * 3	
# x = 5
# x *= 3
# print(x)

# # /=	x /= 3	x = x / 3	
# x = 5
# x /= 3
# print(x)

# # %=	x %= 3	x = x % 3
# x = 5
# x%=3
# print(x)	

# # //=	x //= 3	x = x // 3	
# x = 5
# x//=3
# print(x)

# # **=	x **= 3	x = x ** 3	
# x = 5
# x **= 3
# print(x)

# # &=	x &= 3	x = x & 3	
# x = 5
# x &= 3
# print(x)

# # |=	x |= 3	x = x | 3	
# x = 5
# x |= 3
# print(x)

# # ^=	x ^= 3	x = x ^ 3	
# x = 5
# x ^= 3
# print(x)

# # >>=	x >>= 3	x = x >> 3	
# x = 5
# x >>= 3
# print(x)

# # <<=	x <<= 3	x = x << 3	
# x = 5
# x >>= 3
# print(x)

# # :=	print(x := 3)
# # print(x)
# print(x := 3)

# Python Comparison Operators

# ==	Equal	x == y
# x = 5
# y = 3
# print(x == y)

# !=	Not equal	x != y	
# x = 5
# y = 3
# print(x == y)

# >	Greater than	x > y	
# x = 5
# y = 3
# print(x > y)
# returns True because 5 is greater than 3

# <	Less than	x < y
# x = 5
# y = 3
# print(x < y)
# returns False because 5 is not less than 3	

# >=	Greater than or equal to	x >= y	
# x = 5
# y = 3
# print(x >= y)
# returns True because five is greater, or equal, to 3

# <=	Less than or equal to	x <= y
# x = 5
# y = 3
# print(x <= y)
# returns False because 5 is neither less than or equal to 3

# Python Logical Operators

# and 	Returns True if both statements are true 
# x = 5
# print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10
 	
# or	Returns True if one of the statements is true	
# x = 5
# print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# not	Reverse the result, returns False if the result is true
# x = 5
# print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

# Python Identity Operators

# is 	Returns True if both variables are the same object	x is y	
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is z)
# print(x is y)
# print(x == y)

# is not	Returns True if both variables are not the same object	x is not y
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is not z)
# print(x is not y)
# print(x != y)

# Python Membership Operators

# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# x = ["apple", "banana"]
# print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
# x = ["apple", "banana"]
# print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

# Python Bitwise Operators

# & 	AND	Sets each bit to 1 if both bits are 1	x & y
# print(6 & 3)

# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# print(6 | 3)

# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# print(6 ^ 3)

# ~	NOT	Inverts all the bits	~x	
# print(~3)

# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# print(3 << 2)

# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 
# print(8 >> 2)

