#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
print(a)
print(b)
c = []
d = []

for i in b:
    if i in a:
        c.append(i)
c.sort()
print(c)
#the following code remove all the duplicates in c
test = (len(c))
for x in range(test):
    d.append(c[0])
    test1 = c[0]
    c.remove(c[0])
    if test1 in c:
        print('Duplicate - ' + str(c[0]))
        d.remove(c[0])

print(d)

#import random
#a = random.sample(range(1,30), 12)
#b = random.sample(range(1,30), 16)
#result = [i for i in set(a) if i in b]
