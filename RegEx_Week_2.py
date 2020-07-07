import re
file = open("RegEx_week_2.txt")
sumi = 0
i = 0

for line in file:
    line=line.rstrip()
    sum= re.findall('[0-9]+',line)
    for j in range(len(sum)):
        sumi=sumi+int(sum[j])  
print('sum>>',sumi)
