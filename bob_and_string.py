from sys import stdin,stdout
T = int(stdin.readline())
while T>0:
    dic1= {}
    dic2 = {}
    s = stdin.readline().split()
    t = stdin.readline().split()
    s = s[0]
    t = t[0]
    for x in s:
        if x not in dic1:
            dic1[x] = [True]
        else:
            dic1[x].append(True)

    for x in t:
        if x not in dic2:
            dic2[x] = [True]
        else:
            dic2[x].append(True)
    
    temp=z=0
    
    for i in t:
        if i in dic1:
            try:
                del dic1[i][0]
            except IndexError:
                temp=temp+2
                z=z+1
        else:
            temp=temp+2
            z=z+1
            
    if len(s)!=len(t):
        for i in s:
            if i not in dic2:
                temp=temp+1
            else:
                try:
                    del dic2[i][0]
                except IndexError:
                    temp=temp+1
        temp = temp-z
    
    stdout.write(str(temp)+'\n')
    T=T-1
