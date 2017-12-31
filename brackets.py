from pythonds.basic.stack import Stack

str = input("Enter your input: ")
left = "({["
right = ")}]"
s = Stack()
valid = True
for i in str:
    if i in left:
        s.push(i)
    elif i in right:
        if s.isEmpty():
            valid = False
            break
        elif left.index(s.pop()) != right.index(i):
            valid = False
            break
if valid is True:
    print("best")
else:
    print("not good")

        
    
