# Scenario
# Here is a short story:

# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

# Your task is to:

# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
# now create a new variable named total_apples equal to the addition of the three previous variables.
# print the value stored in total_apples to the console;
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.

john = 3
mary = 5
adam = 6

print(john, + mary, + adam, sep=",") # 3,5,6

total_apples = john + mary + adam
print(total_apples) # = 14

print("Total number of apples: ", + total_apples) # = Total number of apples: 14

mela = 10
gus = 5
geadas = 23
print(geadas * mela - gus) #225 = 23 * 10 - 5 

total_oranges = geadas * mela + gus
print(total_oranges)

total_fruits = total_apples + total_oranges
print(total_fruits)

