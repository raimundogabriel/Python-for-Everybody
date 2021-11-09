#giving back the largest numer in a sequence

def largestNumber(numberList, largestSoFar):
    for numberIndex in numberList:
        if numberIndex > largestSoFar:
            largestSoFar = numberIndex
    return largestSoFar

largestSoFar = -1
numberList = [8, 19, 0, 25, 28, 11]
print('the largest number in the sequence is ', largestNumber(numberList, largestSoFar))