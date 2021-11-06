#creating a simple bank accont program
HOURLIMIT = 60
REGULARHOUR = 1.2
EXTRAHOUR = 1.7

def payCheck(name, workingTime, accontNumber) :
    if workingTime > HOURLIMIT :
        accontNumber = workingTime * REGULARHOUR + ((HOURLIMIT - workingTime) * EXTRAHOUR)
    else:
        accontNumber = workingTime * REGULARHOUR
    return name, 

limit = 0
while limit > 0 :
    
    limit +1
