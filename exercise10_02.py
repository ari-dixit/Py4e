name = input('Enter file name: ')
count = dict()
try :
    handle = open(name)
except :
    print('Enter a valid file name')
    quit()
for line in handle :
    line.strip()
    words = line.split()
    try :
        if words[0] == 'From' :
            time = words[5].split(':')
            if count.get(time[0]) is None :
                count[time[0]] = 1
            else :
                count[time[0]] = count.get(time[0]) + 1
    except :
        continue
newCount = sorted(count)
for key in newCount :
    print(key, count.get(key))
