import random
a = random.sample(range(50),20)
b = [i for i in a if i%2==0]
print(a)
print(b)
