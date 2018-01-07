from sys import stdin,stdout

s = stdin.readline()
freq = {}
for i in s:
    freq[i] = 1 + freq.get(i,0)    #this is the import line

m = max(freq.values())
list1 = [x for x in freq.keys() if freq[x] == m]
s
p=122
for x in list1:
    if ord(x) < p:
        p = ord(x)
        res = x

stdout.write(str(res)+' '+str(freq[res]))
    
