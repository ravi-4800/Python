import numpy as np

t = int(input())
while t>0:
    a = input().split(' ')
    ar = input().split(' ')
    arr = [int(i) for i in ar]
    if min(arr)<int(a[1]):
        print(int(a[1])-min(arr))
    else:
        print(0)
    n=n-1
    
        
        
    
