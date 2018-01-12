n = int(input())
a = [int(i) for i in input().split(" ")]
dic = {i+1:a[i] for i in range(len(a))}

j = 0
while True:
    b = []
    for i in range(2,len(dic)+1):
        if dic[i-1]<dic[i]:
            b.append(i)

    if len(b)!=0:
        j = j+1
    else:
        break
    for i in b:
        del dic[i]


   #### important part
    q=1                    
    dic2 = {}
    for i in dic:
        dic2[q] = dic[i]
        q=q+1
    dic = dic2    
        
print(j)
