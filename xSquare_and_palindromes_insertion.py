n = int(input())

for i in range(n):
    freq = {}
    temp = 0
    s = input()
    for x in s:
        freq[x] = 1+freq.get(x,0)
    for x in freq.values():
        if x%2!=0:
            temp = temp +1
    if temp !=0:
        print(temp-1)
    else:
        print(temp)
    
    
