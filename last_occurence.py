from sys import stdin,stdout
t = int(stdin.readline())
while t>0:
    n = int(stdin.readline())
    arr_ele = stdin.readline().split()
    q = int(stdin.readline())
    for i in range(q):
        x = stdin.readline().split()
        #print(x)
        if x[0] not in arr_ele:
            stdout.write('-1\n')
        else:
            a=max([i for i in range(n-1,-1,-1) if arr_ele[i] == x[0]])+1
            stdout.write(str(a)+'\n')

    t=t-1
        
