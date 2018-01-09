list1 = []
list2 = []
n = int(input())
a = input().split(" ")
for i in range(n):
    if i == 0:
        list1.append(-1)
    else:
        j = i
        while j!=0:
            if int(a[j-1]) > int(a[i]):
                list1.append(j)
                break
            j = j-1
        else:
            list1.append(-1)

    
for i in range(n):
    if i == n-1:
        list2.append(-1)
    else:
        j = i
        while j!=n-1:
            if int(a[j+1]) > int(a[i]):
                list2.append(j+2)
                break
            j = j+1
        else:
            list2.append(-1)

for i in range(n):
    print(list1[i]+list2[i], end = " ")


                                    
