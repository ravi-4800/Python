n = int(input())
a = [int(i) for i in input().split(' ')]
if sum(a) == 2*(n-1):
    print('Yes')
else:
    print('No')
