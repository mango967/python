largest=0
smallest=0
count = 0
total = 0
while True:
    num=input('Enter a number: ')
    if num == 'done':
        break
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue
    count=count+1
    total = total+num
    if count == 1:
        largest = num
        smallest = num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print('Max is ', largest)
print('Min is ', smallest)
print('count is ', count)
print('total is ', total)