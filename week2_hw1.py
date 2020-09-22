import re
f = open("regex_sum_837102.txt")
lst1 = list()
lst2 = list()
ans = 0 
for line in f :
    line = line.rstrip()
    if re.findall('[0-9]+', line) :
        lst1 = re.findall('[0-9]+', line)
        lst2 = lst2 + lst1

for i in lst2 :
    ans = ans + int(i)
print(ans)
