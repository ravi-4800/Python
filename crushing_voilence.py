from collections import Counter
from sys import stdin,stdout
t = int(stdin.readline())
while t>0:
    boys = {}
    girls = {}
    boys_beating = {}
    girls_beating = {}
    n = int(stdin.readline())
    a = stdin.readline().split()
    b = stdin.readline().split()
    for i in range(1,n+1):
        boys[i] = int(a[i-1])
        girls[i] = int(b[i-1])

    ##for boys   
    for i in range(1,n+1):
        if i != girls[boys[i]]:
            boys_beating[i] = girls[boys[i]]

    

    ##for girls
    for i in range(1,n+1):
        if i != boys[girls[i]]:
            girls_beating[i] = boys[girls[i]]

   
    try:
        max_boys_beatings = max(Counter(boys_beating.values()).values())
    except ValueError:
        max_boys_beatings = 0
    try:
        max_girls_beatings = max(Counter(girls_beating.values()).values())
    except ValueError:
        max_girls_beatings = 0
    max_beatings = max(max_boys_beatings,max_girls_beatings)

    temp = 0
    for i in boys:
        if i != girls[boys[i]]:
            if girls[boys[girls[boys[i]]]] == i:
                temp = temp + 1

    for i in girls:
        if i != boys[girls[i]]:
            if boys[girls[boys[girls[i]]]] == i:
                temp = temp + 1

    print("{} {}".format(max_beatings,temp//2))   
    t=t-1
