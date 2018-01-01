t = int(input())
while t>0:
    n = int(input())
    a = input().split(" ")
    dic = {a[y]:True for y in range(n)}
    #print(dic.values())
    #dic = set(a)
    k = int(input())
    #for i in range(k):
    x = input().split(" ")
        #print(x)
    for i in x:    #print(type(x))
        if i in dic:
            print("Yes")
        else:
            print("No")
    t=t-1
