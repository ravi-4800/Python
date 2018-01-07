from sys import stdin,stdout
from collections import Counter
n = int(stdin.readline())
dic = {}
for i in range(n):
    a,b = stdin.readline().split()
    dic.setdefault(a,b)    #this is important part

dic1 = Counter(dic.values())
sorted(dic1)
m = max(dic1.values())
list1 = [x for x in dic1.keys() if dic1[x] == m]

stdout.write(str(list1[0])+'\n')
stdout.write(str(dic1['football']))
