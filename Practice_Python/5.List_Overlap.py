a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)

print(c)

## Extras
import random
list1 = random.sample(range(50),10)
list2 = random.sample(range(50),15)

list3 = set()
print(list1)
print(list2)
list3 = {i for i in list1 if i in list2}
print(list(list3))

