a = [1,4,2,6,34,567,23,9,12,32]
print("Original List: {}".format(a))
for i in a:
    if i<10:
        print(i)
b = [i for i in a if i <6]
print(b)

n = int(input("Enter a number: "))
c = [i for i in a if i<n]
print(c)
