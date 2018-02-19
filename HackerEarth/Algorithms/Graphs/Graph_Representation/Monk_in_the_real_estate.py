t = int(input())
while t>0:
    s = set()
    n = int(input())
    for i in range(n):
        a,b = [int(x) for x in input().split(" ")]
        s.add(a)
        s.add(b)
    print(len(s))
    t -= 1
