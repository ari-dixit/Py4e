large = None
small = None

while True :
    val = input('Enter a number: ')
    try :
        val = int(val)
        if small is None :
            small = val
        if large is None :
            large = val
        if val < small :
            small = val
        if val > large :
            large = val

    except :
        if val == 'done' :
            break
        print('Invalid input')
        continue

print('Maximum is', large)
print('Minimum is', small)
