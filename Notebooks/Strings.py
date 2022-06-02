"""
Strings
    Sequences of chars using either double or single quotes
    Strings = ordered sequences, can use indexing and slicing to grab sub-sections
        Indexing - grab a single character of a string, starting at 0
            can reverse index with 0 -4 -3 -2 -1
    Slicing allows you to grab a subsection of multiple chars, a slice of the string
        Syntax [start:stop(up to but not including):step]
            Step is the size of the jump you take
"""

"""
String Indexing and Slicing
"""

#Indexing
# myString = "Hello World"
# print(myString)

# print(myString[0])
# print(myString[8])
# print(myString[9])
# print(myString[-2]) # negative indexing, grabs l

#Slicing
# Syntax [start:stop(up to but not including):step]

# myString = "abcdefghijk"

# print(mystring[2:])
# print(mystring[:3])
# print(mystring[3:6])
# print(mystring[1:3])

# print(myString[::2]) #Jumps of 2
# print(myString[2:7:2])

# #reversing a string
# print(myString[::-1])

"""
String Immutability
    Cannot change strings
    Can't grab a string char and reassign it
    Can merge two strings wiht concatenation
"""

# name = "Sam"

# lastLetters = name[1:]
# print("P" + lastLetters)

# x = "Hello World"
# print(x + " it is beautiful outside")

# letter = "z"

# print(letter * 10)

"""
String Methods
"""

# x = "Hello World"
# x.upper()

# x.split       creates a list from a string based on whitespace or letter you pass in
# x.split(i)    will split based on location of "i"

"""
String formatting
    known as string interpolation
    .format() method
        'string here {} then also {}'.format('something1','something2')
    f-strings (formatted string literals
"""
# print('This is a string {}'.format('INSERTED'))
# print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

"""
Float formatting follows "{value:width:precision f}
    width is places before the decimal point
    Used for rounding
"""

# result = 100/777
# print(result)
# print("The result was {r:1.3}".format(r = result))

"""
f-string literals
"""

# name = "Nick"
# age = 27
# print(f"Hello, his name is {name}")
# print(f'{name} is {age} years old.')






