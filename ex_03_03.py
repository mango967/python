score = input('Enter Score: ')
Score = float(score)

if Score < 0.0 or Score > 1.0:
    print("Enter Correct Data. ")
    quit()
elif Score >= 0.9:
    print('A')
elif Score >= 0.8:
    print('B')
elif Score >= 0.7:
    print('C')
elif Score >= 0.6:
    print('D')
elif Score < 0.6:
    print('F')

    #problem with getting output even if input is not within range
    #someone else's format which works
