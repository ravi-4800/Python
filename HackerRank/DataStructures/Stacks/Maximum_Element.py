from sys import stdin,stdout
n = int(input())
list1 = []
for i in range(n):
    a = stdin.readline().split()
    if int(a[0]) == 1:
        list1.append(int(a[1]))    
    elif int(a[0]) == 2:
        list1.pop()
    else:
        print(max(list1))
