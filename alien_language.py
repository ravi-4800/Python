n = int(input())
for i in range(n):
    a = input()
    b = input()
    flag = False
    for x in b:
        if x in a:
            print("YES")
            flag = True
            break
    if flag == False:
        print("NO")
