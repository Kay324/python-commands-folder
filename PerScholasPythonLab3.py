#String Data Types

myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "Fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a lot of {} {} !".format(name,color,animal))