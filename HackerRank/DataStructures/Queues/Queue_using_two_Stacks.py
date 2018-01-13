stack1 = []
stack2 = []
q = int(input())
while q>0:
    a = input().split(" ")
    if int(a[0])==1:
        stack1.append(int(a[1]))
    elif int(a[0])==2:
        stack2 = stack1[::-1]
        stack2.pop()
        stack1 = stack2[::-1]
    else:
        stack2 = stack1[::-1]
        print(stack2[-1])
        stack1 = stack2[::-1]
    q=q-1
