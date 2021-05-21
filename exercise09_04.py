name = input('Enter file name: ')
file = open(name)
count = dict()
big = None
for line in file :
    line.strip()
    words = line.split()
    try :
        if words[0] == 'From' :
            if count.get(words[1]) is None :
                count[words[1]] = 1
            else :
                count[words[1]] = count.get(words[1]) + 1
    except :
        continue
    for key in count :
        if big == None or count[key] > count[big] :
            big = key
print(big, count.get(big))
