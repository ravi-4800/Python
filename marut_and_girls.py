from sys import stdin,stdout
n = int(stdin.readline())
a = stdin.readline().split()
m = int(stdin.readline())
res=0
for i in range(m):
    x = stdin.readline().split()
    dic = {j:True for j in x}
    temp=0
    for y in a:
        if y in dic:
            temp=temp+1
            if temp==n:
                res = res+1
                break
stdout.write(str(res))
