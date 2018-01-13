s = input("Enter a string: ")
i=0
j=-1
temp = 0
while i<=len(s)//2-1 and j>=-(len(s)//2):
    if s[i]==s[j]:
        temp = temp+1
        print(temp)
    else:
        break
    i = i+1
    j = j-1
if temp == len(s)//2:
    print("String is palindrome")
else:
    print("String is not palindrome")

#### using reverse string
p = input("Enter a string: ")
if (p == p[::-1]):
    print("String is palindrome")
else:
    print("String is not palindrome")
