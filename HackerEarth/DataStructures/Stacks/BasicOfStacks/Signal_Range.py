from sys import stdin,stdout
t = int(input())
while t>0:
    n = int(input())
    #list1 = [int(i) for i in input().split(" ")]  ##this line is not working here
    list2 = stdin.readline().split()
    list1 = [int(i) for i in list2]
    dic = {}
    stack1 = []
    stack2 = []

    dic[list1[0]] = [1]
    stack1.append(list1[0])
    for i in range(1,n):
        temp = 1

        while(len(stack1)!=0 and list1[i]>stack1[len(stack1)-1]):
            stack2.append(stack1.pop())
            temp = temp+1
            
        while len(stack2)!=0:
            stack1.append(stack2.pop())
        stack1.append(list1[i])
        
        if list1[i] not in dic:
            dic[list1[i]] = [temp]
        else:
            dic[list1[i]].append(temp)

    for i in list1:
        stdout.write(str(dic[i][0])+" ")
        del dic[i][0]
    stdout.write("\n")
    t=t-1
        
        
        
