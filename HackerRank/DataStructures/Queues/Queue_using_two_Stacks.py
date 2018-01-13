from collections import deque
q = int(input())
que = deque()
while q>0:
    a = input().split(" ")
    if int(a[0])==1:
        que.append(int(a[1]))
    elif int(a[0])==2:
        que.popleft()
    else:
        print(que[0])
