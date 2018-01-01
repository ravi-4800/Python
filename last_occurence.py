t = int(input())
while t>0:
    n = int(input())
    arr_ele = input().split(' ')
    q = int(input())
    for i in range(q):
        x = input()
    
        if x not in arr_ele:
            print(-1)
        else:
            for i in range(n-1,-1,-1):
                if arr_ele[i] == x:
                    print(i+1)
                    break
    t=t-1
