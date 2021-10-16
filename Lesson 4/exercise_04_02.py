#Program that gives the Score based on the grade
score = input("Enter Score: ")
#trying if score is a number
try :
    fScore = float(score)
except :
    print("Bad score!")
if fScore < 0.0 or fScore > 1.0 :
    print("Bad Score!")
elif fScore >= 0.9 :
    print("A")
elif fScore >= 0.8 :
    print("B")
elif fScore >= 0.7 :
    print("C")
elif fScore >= 0.6 :
    print("D")
else :
    print("F")
print("Done!")