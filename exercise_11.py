import re

name = 'regex_sum_1223586.txt'
sum = 0

for line in open(name) :
    numbers = re.findall('[0-9]+', line)
    print(numbers)
    for num in numbers :
        realnum = float(num)
        sum = sum + realnum

print(sum)
