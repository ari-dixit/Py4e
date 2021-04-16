# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print('Invalid File Name:', fname)
    quit()
for line in fh : 
    text = line.rstrip()
    print(text.upper())
