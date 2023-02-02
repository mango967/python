score = input('Enter : ')

try:
    Score = float(score)
except:
    print('Enter a valid numerical number')
    quit()

def test(score):
    if score < 0.0 or score > 1.0:
        print('Enter a number between 0 and 1')
        quit()
    elif score >= 0.9:
        result = 'A'
    elif score >= 0.8:
        result = 'B'
    elif score >= 0.7:
        result = 'C'
    elif score >= 0.6:
        result = 'D'
    elif score < 0.6:
        result ='F'
    return result

mark=test(Score)
print('Score: ', mark)