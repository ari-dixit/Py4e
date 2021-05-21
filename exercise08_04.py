fname = input('Enter a file name: ')
try :
    fh = open(fname)
except :
    print('Enter a valid file name:', fname)
    quit()
words = list()
for line in fh :
    sentence = line.split()
    for word in sentence :
        if word not in words :
            words.append(word)
words.sort()
print(words)
