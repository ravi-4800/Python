n = int(input())
a = [int(i) for i in input().split(" ")]
i = 0
top = 0
area = 0
maxArea = 0
stack = []
while i<len(a):
    if len(stack)==0 or a[stack[-1]]<=a[i]:
        stack.append(i)
        i = i + 1     # important line, it is creating loop
    else:
        top = stack.pop()
        if len(stack)==0:
            area = a[top]*i
        else:
            area = a[top] * (i-stack[-1]-1)
        if area > maxArea:
            maxArea = area

while len(stack)!=0:
    top = stack.pop()
    if len(stack)==0:
        area = a[top]*i
    else:
        area = a[top] * (i-stack[-1]-1)
    if area > maxArea:
        maxArea = area

print(maxArea)
    
            
            
