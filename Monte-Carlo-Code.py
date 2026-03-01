import random
trials = 10000
n = 0
total = 0
number_counter = 0
lst_of_counter = []
while n < trials:
    while total <= 1:
        number = random.random()
        total += number
        number_counter += 1
    total = 0
    lst_of_counter.append(number_counter)
    number_counter = 0
    n += 1
e = sum(lst_of_counter)/len(lst_of_counter)
print(e)
