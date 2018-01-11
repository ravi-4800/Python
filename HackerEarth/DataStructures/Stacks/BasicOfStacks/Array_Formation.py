from sys import stdout

def prime(a):
    for i in range(2,a//2+1):
        if a%i == 0:
            return 2
    else:
        return 1

n = int(input())
list1 = []
list2 = []
a = [int(i) for i in input().split(" ")]
for i in a:
    if prime(i)==1:
        list1.append(i)
    else:
        list2.append(i)
for j in list1:
    stdout.write(str(j)+" ")
stdout.write("\n")
list2.reverse()
for j in list2:
    stdout.write(str(j)+" ")
##for k in range(len(list2)):
##    stdout.write(str(list2.pop())+" ")
        
        
