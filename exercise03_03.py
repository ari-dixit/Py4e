score = input("Enter Score: ")

try :
    score = float(score)
    if 0.0 > score or score > 1.0 :
        print('Enter a number from accepted range')
        quit()
except :
    print('Enter a valid input')
    quit()

if score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
else :
    print('F')
