from sys import stdin,stdout
t = int(stdin.readline())
dic = {}
while t>0:
    n = int(stdin.readline())
    arr_ele = stdin.readline().split()
    dic = {arr_ele[y]:y for y in range(n)}
    q = int(stdin.readline())
    for i in range(q):
        x = stdin.readline().split()
        if x[0] not in dic:
            print(-1)
        else:
            print(dic[x[0]]+1)
    t=t-1
