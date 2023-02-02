hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate:")
r=float(rate)
if h>40:
    print("Overtime")
    reg = h*r
    ot = (h-40)*0.5*r
    pay = reg + ot
else:
    print("Regular")
    pay=h*r
print("Pay:", pay)