fname = input('Enter a file name: ')
try :
    fh = open(fname)
except :
    print('Enter a valid file name:', fname)
    quit()
emails = list()
parts = None
for line in fh :
    parts = line.split()
    if len(parts) < 1 :
        continue
    if parts[0] == 'From' :
        emails.append(parts[1])
    # try :
    #     if parts[0] == 'From' :
    #         emails.append(parts[1])
    # except :
    #     continue
for email in emails :
    print(email)
print('There were', len(emails), 'lines in the file with From as the first word')
