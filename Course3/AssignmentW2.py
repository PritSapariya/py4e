# Course 3 --> Week 2 --> Regular Expression Assignment
# Resources --> regex_sum_634318.txt

import re
conut = 0
sum = 0 

handle = open('regex_sum_634318.txt')

for line in handle :
    line = line.strip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0 : 
        for word in stuff :
            conut = conut + 1
            sum = sum + int(word)

print(sum)