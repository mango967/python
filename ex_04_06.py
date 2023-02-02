hours=input("Enter Hours:")
rate=input("Enter rate:")
try:
    h = float(hours)
    r = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

def computepay(hours, rate) :
    if hours>40:
        reg = hours*rate
        ot = (hours-40)*0.5*rate
        pay = reg + ot
    else:
        pay=hours*rate
    return pay
   
pay = computepay(h, r)
print("Pay", pay)
