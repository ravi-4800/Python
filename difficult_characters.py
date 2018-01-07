from sys import stdin,stdout
from collections import Counter
import string

t = int(input())
for i in range(t):
    s = input()
    dic = {}
    
    for x in s:
        dic[x] = 1+dic.get(x,0)
    dic1 = Counter(dic.values())
   
    for x in list(reversed(string.ascii_lowercase)):
        if x not in dic:
            stdout.write(str(x)+' ')

    for x in list(sorted(dic1.keys())):
        list1 = []
        for y in dic:
            if dic[y] == x:
                list1.append(ord(y))

        list1.sort()
        for y in list(reversed(list1)):
            stdout.write(str(chr(y))+' ')
    stdout.write('\n')
        
                
                
                
            
        
    
