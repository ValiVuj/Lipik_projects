import random
n = 36
li = []
for i in range(n):
    li.append(random.randint(0,1001))
print(li)
print(len(li))
median = (len(li) + 1) / 2
print(median)


