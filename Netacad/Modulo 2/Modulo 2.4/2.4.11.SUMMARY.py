# 2.4.11 SECTION SUMMARY
# A variable is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. (2.1.4.1)

# Each variable must have a unique name ‒ an identifier. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore(_), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive.

# Python is a dynamically-typed language, which means you don't need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (=) sign, i.e., var = 1.

# You can also use compound assignment operators (shortcut operators) to modify values assigned to variables, for example: var += 1, or var /= 5 * 2.

# You can assign new values to already existing variables using the assignment operator or one of the compound operators, for example:

var = 2
print(var) #=2
 
var = 3
print(var) #=3
 
var += 1
print(var) #=4

var = "007"
print("Agent " + var)