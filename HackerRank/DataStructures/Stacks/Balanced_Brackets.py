left = '({['
right = ')}]'

n = int(input())
for j in range(n):
    stack=[]
    flag = True
    s = input()
    for i in s:
        if i in left:
            stack.append(i)
            
        else:
            if len(stack) == 0:
                flag = False
                break
            elif left.index(stack.pop()) != right.index(i):
                
                flag = False
                break
            
    if flag == True and len(stack)==0:
        print('YES')
    else:
        print('NO')
        
        
