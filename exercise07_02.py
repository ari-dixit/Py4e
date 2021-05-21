# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print('Invalid File Name:', fname)
num = None
colon = None
val = None
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    num = line.strip()
    colon = num.find(':')
    val = float(num[colon+1:].strip())
    total = total + val
    count = count + 1
avg = total/count
print('Average spam confidence:', avg)
