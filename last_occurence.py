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
            #print(max([arr_ele.index(i) for i in arr_ele if i == x])+1)
            print(max([i for i in range(n) if arr_ele[i] == x])+1)
    t=t-1
        
