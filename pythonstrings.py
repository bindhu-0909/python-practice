# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = "Hello"
# print(a)

# assign a multiline string to a variable by using three quotes:

#  a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# or three single quotes:



# Square brackets can be used to access elements of the string.

#Strings are Arrays [list to store]
# a = "Hello, World!"
# print(a[1])



# Looping Through a String
# for x in "banana":
#   print(x)
 
# we can loop through the characters in a string, with a for loop.



# String Length
# To get the length of a string, use the len() function.

# a = "Hello, World!"
# print(len(a))

# number of characters in the line



# Check String
# spelling name and adding a spcecial symbol that proves if spelled right

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")



# Check if NOT
# to check if a certain phrase or character is NOT present

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")



# Slicing

# b = "Hello, World!"
# print(b[2:5])

# total no of chars 12
# 1st index is 6 because to not print "hello, "
# aaab
# b = "Hello, World!"
# print(b[-6:0])

# this is a new change

# Upper Case
# a = "Hello, World!"
# print(a.upper()) 

# lower case
# a = "Hello, World!"
# print(a.lower())

# Remove Whitespace
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# Replace String
# a = "Hello, World!"
# print(a.replace("H", "J"))

# Split String
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# String Format

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# F-Strings

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# Placeholders and Modifiers

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars" "2 decimals"
# print(txt)

# txt = f"The price is {20 * 59} dollars" "*multiply"
# print(txt)

# Escape Character "\"

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)


# \'	Single Quote
# txt = 'It\'s alright.'
# print(txt) 	

# \\	Backslash
# txt = "This will insert one \\ (backslash)."
# print(txt) 	

# \n	New Line	
# txt = "Hello\nWorld!"
# print(txt) 

# \r	Carriage Return	
# txt = "Hello\rWorld!"
# print(txt) 

# \t	Tab	
# txt = "Hello\tWorld!"
# print(txt)

# \b	Backspace	
#This example erases one character (backspace):
# txt = "Hello \bWorld!"
# print(txt) 

# \f	Form Feed	
# move to new page or erase the screen

# \ooo	Octal value	
#A backslash followed by three integers will result in a octal value:
# txt = "\110\145\154\154\157"
# print(txt)                    - doubt (not understood what it does or is used for)

# \xhh	Hex value
# A backslash followed by an 'x' and a hex number represents a hex value:
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt)                  -same doubt

# String capitalize() Method
# txt = "python is FUN!"
# x = txt.capitalize()
# print (x)

# String casefold() Method
# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# String center() Method
# txt = "banana"
# x = txt.center(20) space of 20 chras
# print(x)

# String count() Method  Returns the number of times a specified value occurs in a string
# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x)

# String encode() Method   Returns an encoded version of the string
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)

# String endswith() Method    Returns true if the string ends with the specified value
# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

# expandtabs()	Sets the tab size of the string
# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(2)
# print(x)

# String find() Method
# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)

# format()	Formats specified values in a string
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# format_map()	Formats specified values in a string

# String index() Searches the string for a specified value and returns the position of where it was found
# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.index("e")
# print(x)

# isalnum()	Returns True if all characters in the string are alphanumeric
# txt = "Company12"
# x = txt.isalnum()
# print(x)

# String isalpha() Returns True if all characters in the string are in the alphabet
# txt = "CompanyX"
# x = txt.isalpha()
# print(x)

# isascii()	Returns True if all characters in the string are ascii characters
# txt = "Company123"
# x = txt.isascii()
# print(x)
# ascii- letterm, symols, numbers

# isdecimal()	Returns True if all characters in the string are decimals
# txt = "1234"
# x = txt.isdecimal()
# print(x)

# isdigit()	Returns True if all characters in the string are digits
# txt = "50800"
# x = txt.isdigit()
# print(x)

# isidentifier()	Returns True if the string is an identifier
# txt = "Demo"
# x = txt.isidentifier()
# print(x)

# identifier- (a-z),(0-9),(__)

# islower()	Returns True if all characters in the string are lower case
# txt = "hello world!"
# x = txt.islower()
# print(x)

# isnumeric()	Returns True if all characters in the string are numeric
# txt = "565543"
# x = txt.isnumeric()
# print(x)

# isprintable()	Returns True if all characters in the string are printable
# txt = "Hello! Are you #1?"
# x = txt.isprintable()
# print(x)

# txt = "Hello!\nAre you #1?"
# x = txt.isprintable()
# print(x)

# isspace()	Returns True if all characters in the string are whitespaces
# txt = "   "
# x = txt.isspace()
# print(x)

# txt = "   s   "
# x = txt.isspace()
# print(x)

# istitle()	Returns True if the string follows the rules of a title
# txt = "Hello, And Welcome To My World!"
# x = txt.istitle()
# print(x)

# isupper()	Returns True if all characters in the string are upper case
# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)

# join()	Joins the elements of an iterable to the end of the string
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# ljust()	Returns a left justified version of the string
# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.")

# lower()	Converts a string into lower case
# txt = "Hello my FRIENDS"
# x = txt.lower()
# print(x)

# lstrip()	Returns a left trim version of the string
# txt = "     banana     "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite")

# maketrans()	Returns a translation table to be used in translations
# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))

# partition()	Returns a tuple where the string is parted into three parts
# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x)

# replace()	Returns a string where a specified value is replaced with a specified value
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

# rfind()	Searches the string for a specified value and returns the last position of where it was found
# txt = "Mi casa, su casa."
# x = txt.rfind("casa")
# print(x)

# rindex()	Searches the string for a specified value and returns the last position of where it was found
# txt = "Mi casa, su casa."
# x = txt.rindex("casa")
# print(x)

# rjust()	Returns a right justified version of the string/
# txt = "banana"
# x = txt.rjust(20)
# print(x, "is my favorite fruit.")

# rpartition()	Returns a tuple where the string is parted into three parts
# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("bananas")
# print(x)

# rsplit()	Splits the string at the specified separator, and returns a list
# txt = "apple, banana, cherry"
# x = txt.rsplit(", ")
# print(x)

# rstrip()	Returns a right trim version of the string
# txt = "     banana     "
# x = txt.rstrip()
# print("of all fruits", x, "is my favorite")

# split()	Splits the string at the specified separator, and returns a list
# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# splitlines()	Splits the string at line breaks and returns a list
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

# startswith()	Returns true if the string starts with the specified value
# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello")
# print(x)

# strip()	Returns a trimmed version of the string
# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

# title()	Converts the first character of each word to upper case
# txt = "Welcome to my world"
# x = txt.title()
# print(x)

# translate()	Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# mydict = {83:  80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))

# upper()	Converts a string into upper case
# txt = "Hello my friends"
# x = txt.upper()
# print(x)

# zfill()	Fills the string with a specified number of 0 values at the beginning
# txt = "50"
# x = txt.zfill(10)
# print(x)
