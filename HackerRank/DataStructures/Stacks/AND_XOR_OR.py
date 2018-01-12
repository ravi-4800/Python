from collections import deque

def nextSmallest(p):
    q = deque(p)
    q.remove(min(q))
    return min(q)

maxRes = 0
n = int(input())
a = [int(i) for i in input().split(" ")]
for i in range(len(a)-1):
    for j in range(i+2,len(a)+1):
        m1 = min(a[i:j])
        m2 = nextSmallest(a[i:j])
        res = (((m1 & m2)^(m1 | m2)) & (m1 ^ m2))
        if res > maxRes:
            maxRes = res
print(maxRes)
