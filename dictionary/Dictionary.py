thisDict = {
    "Brand": "Ford",
    "model": "Mustang",
    "year" : "1964"
}
del thisDict["model"]
print(thisDict)

myDict = thisDict.copy()
print(myDict)

thisDict.clear()
print(thisDict)