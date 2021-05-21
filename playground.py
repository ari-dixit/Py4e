print('Welcome to Python Trivia!')
name = input('Contestant Name: ')
print('Alright,', name + ', get ready!')
print('---')
print('First Question: When was Python created?')
print('a) 1980')
print('b) 2001')
print('c) 1976')
print('d) 1998')
print('---')
answer = input('Your Answer: ')
if answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd' :
    print('Not an answer choice!')
    quit()
if answer == 'a' :
    print('Correct!')
else :
    print('Incorrect!')
