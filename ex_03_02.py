hrs = input("Enter Hours:")
rate=input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

if h > 40:
    reg = h*r
    ot = (h-40)*0.5*r
    pay = reg + ot
else:
    pay=h*r
print("Pay:", pay)
