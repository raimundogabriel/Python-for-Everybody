#exercises and examples of conditional Sentences
x=5
if x == 5 :
    print('Equal to 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 :
    print('Less than 6')
if x<=5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not Equal 6')
#using if and else
y = 4
if y > 2 :
    print('Bigger')
else:
    print('Smaller')
print('All done!')
#using if, else and elif
z=11
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('Done')
#try and except strucutres
aux = 'bob'
try :
    istr = int(aux)
except :
    istr = -1
print('Done',istr)
#real situation - a user enters a text insted of a number
getNumber = input('Enter a number: ')
try :
    convert = int(getNumber)
except :
    convert = -1

if convert > 0 :
    print('Nice Job!')
else :
    print('Not a Number!')