#Working with Lists, Tuples, and Dictionaries

#Make a list of fruits
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Print out the list one by one
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Change the cherry to orange
myFruitList[2] = "orange"
print(myFruitList)

#Make a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Print out the tuple one by one
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Introduces the Dictionary Value Tyoe
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Show their fav fruit
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
