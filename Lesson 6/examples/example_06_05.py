#Finding the Average in a loop
controller = 1
listOfNumbers = []
count = 0
sum = 0
print('Ènter the numbers')
#The user will create a list of numbers
while controller > 0 :
    try :
        controller = int(input())
    except :
        print('I said NUMBERS, try again...')
        continue
    print ('negative number get you out')
    if controller >= 0 :
        listOfNumbers.append(controller)
    else :
        break
#The average will be calculated
for value in listOfNumbers :
    count =+ 1
    print(listOfNumbers)
    sum =+ value

print('The Average is ', sum / count)
