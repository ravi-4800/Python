n = int(input())
for i in range(n):
    a = input()
    temp=0
    flag = False
    for j in a:
        if j in a[temp+1:]:
            print("Yes")
            flag = True
            break
        else:
            temp=temp+1
    if flag == False:
        print("No")
