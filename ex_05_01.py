num =0
total = 0
while True :
    value=input('Enter a number: ')
    if value == 'done':
        break
    try:
        v=float(value)
    except:
        print('Invalid input')
        continue
    print(v)
    num = num + 1
    total = total + num

print('Done!')
print(total, num, total/num)
