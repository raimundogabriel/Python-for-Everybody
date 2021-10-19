#what is the 
def computePay(h,r):
    if h <= 40 :
        return h * r
    else :
        base = h * r
        extra = (h - 40) * r * 0.5
        result = base + extra
        return result

hours = float(input('enter your hour: '))
rate = float(input('enter your rate: '))
print('Your paycheck is: ',computePay(hours,rate))