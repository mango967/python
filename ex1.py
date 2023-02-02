num1=input("Enter a number: ")
num2=input("Enter another number: ")

try:
    n = float(num1)
    m = float(num2)
except:
    print('Not a valid number')
    quit()

def multiplication_or_sum(num1,num2):
    product = num1*num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result=multiplication_or_sum(n, m)
print('The result is', result)

# not sure how to make it continue despite an invalid input

