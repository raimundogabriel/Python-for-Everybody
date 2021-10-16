#program that gets hours and rate worked and calculate even it gets extra
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
#now calculates differently if it gets extra hours 
if h < 40 :
    result = h * r
else :
    regular = h * r
    extra = (h - 40) * (r * 0.5)
    result = regular + extra    
print('Your paycheck is: ',result)
    