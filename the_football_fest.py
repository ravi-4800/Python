from sys import stdin,stdout
t = int(stdin.readline())
while t>0:
    list1 = []
    a,b = stdin.readline().split()
    list1.append(b)
    for i in range(int(a)):
        x = stdin.readline().split()
        if x[0] == "P":
            list1.append(x[1])
        else:
            list1.append(list1[len(list1)-2])
    print("Player "+list1[len(list1)-1])
    t = t-1
        
        
