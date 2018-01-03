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

    temp = 0

    for x in t:
        if x in dic1:
            try:
                del dic1[x][0]
            except IndexError:
                temp=temp+1
        else:
            temp=temp+1
                

    for x in s:
        if x in dic2:
            try:
                del dic2[x][0]
            except IndexError:
                temp=temp+1
        else:
            temp=temp+1

    print(temp)
    T=T-1
                
    

