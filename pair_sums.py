from sys import stdin,stdout

a,b = stdin.readline().split()
dic = {}
v = stdin.readline().split()
for i in v:
    if int(i) not in dic:
        dic[int(i)] = [True]      ##concept of multimap
    else:
        dic[int(i)].append(True)
    
temp = 0
flag = False
for i in dic:
    if int(b)-i in dic and int(b)-i!=i:
        flag = True
        print("YES")
        break
    elif int(b)-i in dic and int(b)-i==i:
        if len(dic[int(b)-i]) != 1:
            flag = True
            print("YES")
            break
    
if flag == False:
    print("NO")
            
