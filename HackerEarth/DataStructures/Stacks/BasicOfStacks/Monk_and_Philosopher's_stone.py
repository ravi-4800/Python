n = int(input())
a = [int(i) for i in input().split(" ")]
stack = []
x,y = [int(i) for i in input().split(" ")]
temp = res = 0

for i in range(x):
    inst = input()
    if inst == "Harry":
        stack.append(a[temp])
        if sum(stack)==y:
            res = res+1
            break
        elif sum(stack)!=y and temp == len(a)-1:
            res = -1
            break
        temp = temp+1
        res = res +1
    else:
        stack.pop()
        res = res-1
print(res)
        
