import re

#data = open('regex_sum_42.txt')
data = open('regex_sum_461511.txt')
total_sum = 0
for line in data:
    numbers = re.findall('[0-9]+', line)
    numbers = list(map(lambda x: int(x), numbers))
    total_sum += sum(numbers)

print(total_sum) 
