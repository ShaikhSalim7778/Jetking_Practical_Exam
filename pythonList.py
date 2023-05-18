def getUniqueElement(inputList):
    uniqueList = []

    for element in inputList:
        if element not in uniqueList:
            uniqueList.append(element)

        return uniqueList

    myList = [1, 2, 3, 4, 5, 6, 7,8,9]
    result = getUniqueElement(myList)
    print(result)