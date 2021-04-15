h = input('Enter hours: ')
r = input('Enter rate: ')

hours = float(h)
rate = float(r)

def computepay() :
    if hours > 40 :
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    else :
        pay = hours * rate
    return pay

print('Pay', computepay())
