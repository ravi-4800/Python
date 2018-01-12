from collections import deque

##def smaller(a,b,c):
##    if a!=b and b!=c and a!=c:
##        if a>b and a>c:
##            return a
##        elif b>c and b>a:
##            return b
##        elif c>a and c>b:
##            return c
##    elif a==b and a!=c:
##        if a>c:
##            return a
##        else:
##            return c
##h1 = deque()
##h2 = deque()
##h3 = deque()

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
p1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
p2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
p3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1 = deque(p1)
h2 = deque(p2)
h3 = deque(p3)
#print(type(h1))
##print(h1)
##print(h2)
##print(h3)
##h1 = [h1[i] for i in range(len(h1)-1,-1,-1)]
##h2 = [h2[i] for i in range(len(h2)-1,-1,-1)]
##h3 = [h3[i] for i in range(len(h3)-1,-1,-1)]
##print(h1)
##print(h2)
##print(h3)

##dic = {sum(i):i for i in [h1,h2,h3]}

small = min(sum(h1),sum(h2),sum(h3))

if sum(h1)==small:
    while sum(h1)>=0:
        temp = 1
        while sum(h2)>sum(h1):
            h2.popleft()
        if sum(h1)==sum(h2):
            temp = temp+1
        while sum(h3)>sum(h1) and temp == 2:
            h3.popleft()
        if sum(h3) == sum(h1):
            temp = temp+1
        if temp==3:
            print(sum(h1))
            break
        h1.popleft()
elif sum(h2)==small:
    while sum(h2)>=0:
        temp = 1
        while sum(h1)>sum(h2):
            h1.popleft()
        if sum(h1)==sum(h2):
            temp = temp+1
        while sum(h3)>sum(h2) and temp == 2:
            h3.popleft()
        if sum(h3) == sum(h2):
            temp = temp+1
        if temp==3:
            print(sum(h2))
            break
        h2.popleft()
elif sum(h3)==small:
    while sum(h3)>=0:
        temp = 1
        while sum(h2)>sum(h3):
            h2.popleft()
        if sum(h3)==sum(h2):
            temp = temp+1
        while sum(h1)>sum(h3) and temp == 2:
            h1.popleft()
        if sum(h3) == sum(h1):
            temp = temp+1
        if temp==3:
            print(sum(h1))
            break
        h3.popleft()
