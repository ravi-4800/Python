n = int(input())
s = []
stack1 = []
stack2 = []
for i in range(n):
    a = input().split(" ")
    if int(a[0])==1:
        s = s + list(a[1])
        stack1.append(a[1])
        stack2.append(1)
    elif int(a[0])==2:
        stack1.append(''.join(s[len(s)-int(a[1]):]))
        del s[len(s)-int(a[1]):]
        stack2.append(2)
    elif int(a[0])==3:
        print(s[int(a[1])-1])
    else:
        if stack2[-1]==2:
            s = s + list(stack1.pop())
            stack2.pop()
        else:
            del s[(len(s)-len(stack1.pop())):] ## important
            stack2.pop()

    
    
        
