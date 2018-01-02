from sys import stdin,stdout
n = int(stdin.readline())
sum1 = []
dic1 = {}
dic2 = {}
dic3 = {}

for i in range(n):
    a, b = stdin.readline().split()
    sum1.append(int(a)+int(b))
    if int(a)+int(b) not in dic1:
        dic1[int(a)+int(b)] = i
    else:
        dic2[int(a)+int(b)] = i
    dic3[i] = int(a)

sum1.sort()
temp = 0
for i in sum1:
    if temp==1:
        temp = 0
        continue
    if i in dic1 and i in dic2:
        if dic3[dic1[i]] < dic3[dic2[i]]:
            stdout.write(str((dic1[i]+1))+" ")
            stdout.write(str((dic2[i]+1))+" ")
        else:
            stdout.write(str((dic2[i]+1))+" ")
            stdout.write(str((dic1[i]+1))+" ")
        temp = 1
    else:
        stdout.write(str((dic1[i]+1))+" ")
        temp = 0
    
    

